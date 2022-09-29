from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('Email did not come')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not password:
            raise TypeError('Password did not come')
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


GENDER = (
    (0, 'None'),
    (1, 'Male'),
    (2, 'female'),
)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True, verbose_name=_('Email'), db_index=True, null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name=_('Ismi'))
    last_name = models.CharField(max_length=100, verbose_name=_('Familiyasi'))
    username = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Username')
    phone = models.CharField(max_length=9, unique=True, db_index=True, null=True, blank=True, verbose_name='Raqami*',
                             help_text=_('9 ta raqam bolishi kerak, masalan: 979998877'))
    gender = models.IntegerField(choices=GENDER, default=0, verbose_name=_('Jinsi'))
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name=_('Active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Xodim'))
    is_admin = models.BooleanField(default=False, verbose_name=_('Admin foydalanuvchi'))
    is_superuser = models.BooleanField(default=False, verbose_name=_('Super foydalanuvchi'))
    date_login = models.DateTimeField(auto_now=True, verbose_name=_('Yangilangan sanasi'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Yaratilgan sanasi'))

    objects = AccountManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.last_name and self.first_name:
            return f'{self.last_name} {self.first_name}'
        return self.email

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def token(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data
