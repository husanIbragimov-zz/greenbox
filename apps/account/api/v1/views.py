from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate

from .serializers import RegisterSerializer, LoginSerializer, EmailVerificationSerializer, SetNewPasswordSerializer, \
    ChangeNewPasswordSerializer, ResetPasswordSerializer, AccountSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics, status, permissions, exceptions
from rest_framework.views import APIView
from .permissions import IsAuthenticated
from apps.account.models import Account
from django.conf import settings
from drf_yasg import openapi
from .utils import Util
import jwt


class AccountRegisterAPIView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/v1/register/
    serializer_class = RegisterSerializer

    # user create
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # user details or data
        user_data = serializer.data
        user = Account.objects.get(email=user_data['email'])

        # get refresh token
        token = RefreshToken.for_user(user)

        # activate account with email
        current_site = 'localhost:8000/'
        relative_link = 'account/v1/verify-email/'
        abs_url = f'http://{current_site}{relative_link}?token={str(token.access_token)}'
        email_body = f'Hi, {user.email} \nUser link below to activate your email \n {abs_url}'
        data = {
            'to_email': user.email,
            'email_subject': 'Activate email to Pharma',
            'email_body': email_body
        }
        Util.send_email(data)

        return Response({
            'success': True,
            'message': 'Activate url was sent your email'
        }, status=status.HTTP_201_CREATED)


class EmailVerificationAPIView(APIView):
    # http://127.0.0.1:8000/account/v1/verify-email/?token={token}/
    serializer_class = EmailVerificationSerializer
    permission_classes = (AllowAny,)
    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Verify email',
                                           type=openapi.TYPE_STRING)

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = Account.objects.get(id=payload['user_id'])
            if not user_id.is_active:
                user_id.is_active = True
                user_id.save()
            return Response({
                'success': True,
                'message': 'Email successfully activated'
            }, status=status.HTTP_201_CREATED)
        except jwt.ExpiredSignatureError as e:
            return Response({
                'success': False,
                'message': f'Verification expired | {e.args}'
            }, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response({
                'success': False,
                'message': f'Invalid token | {e.args}'
            }, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/v1/login/
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({
                'success': True,
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Credentials is not valid'
        }, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/v1/reset-password/
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        user = Account.objects.filter(email=request.data['email']).first()

        if user:
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = 'localhost:8000/'
            abs_url = f'http://{current_site}account/v1/set-password-confirm/?uidb64={uidb64}&token={token}/'
            email_body = f'Hello, \n User link below to activate your email \n {abs_url}'
            data = {
                'to_email': user.email,
                'email_subject': 'Reset password',
                'email_body': email_body
            }
            Util.send_email(data)

            return Response({
                'success': True,
                'message': 'Link sent to email'
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Email did not match'
        }, status=status.HTTP_400_BAD_REQUEST)


class SetPasswordConfirmAPIView(APIView):
    # http://127.0.0.1:8000/account/v1/set-password-confirm/<uidb64>/<token>/
    permission_classes = (AllowAny,)

    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = Account.objects.filter(id=id).first()
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({
                    'success': False,
                    'message': 'Token is not valid, please try again'
                }, status=status.HTTP_406_NOT_ACCEPTABLE)
        except DjangoUnicodeDecodeError as e:
            return Response({
                'success': False,
                'message': f'DecodeError: {e.args}'
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            'success': True,
            'message': 'Successfully checked',
            'uidb64': uidb64,
            'token': token
        }, status=status.HTTP_200_OK)


class SetNewPasswordCompletedAPIView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/v1/set-password-completed/
    serializer_class = SetNewPasswordSerializer
    permission_classes = (AllowAny,)

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({
                'success': True,
                'message': 'Successfully set new password'
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Credentials is invalid'
        }, status=status.HTTP_406_NOT_ACCEPTABLE)


class ChangePasswordCompletedAPIView(generics.GenericAPIView):
    # http://127.0.0.1:8000/account/v1/change-password/
    # queryset = Account.objects.all()
    serializer_class = ChangeNewPasswordSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request):
        username = request.user.username
        old_password = request.data['old_password']
        user = authenticate(username=username, password=old_password)
        if not user:
            raise exceptions.AuthenticationFailed({'message': 'Password is not correct'})
        else:
            serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = request.data['password']
        user.set_password(password)
        user.save()
        return Response({
            'success': True,
            'message': 'Successfully set new password'
        }, status=status.HTTP_200_OK)


class MyAccountAPIView(generics.RetrieveUpdateAPIView):
    # http://127.0.0.1:8000/account/v1/profile/{email}/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'username'
