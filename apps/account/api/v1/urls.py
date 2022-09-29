from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.AccountRegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('verify-email/', views.EmailVerificationAPIView.as_view(), name='verify-email'),
    path('reset-password/', views.ResetPasswordAPIView.as_view(), name='reset-password'),
    path('set-password-confirm/<str:uidb64>/<str:token>/', views.SetPasswordConfirmAPIView.as_view(),
         name='set-password-confirm'),
    path('set-password-completed/', views.SetNewPasswordCompletedAPIView.as_view(), name='set-password-completed'),
    path('change-password/', views.ChangePasswordCompletedAPIView.as_view(),
         name='change-password-completed'),
    path('profile/<str:username>/', views.MyAccountAPIView.as_view(), name='profile'),
]
