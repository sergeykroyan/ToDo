from django.db import models
import jwt
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractBaseUser,\
    PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if username is None:
            raise ValueError('User must have a username.')
        if email is None:
            raise ValueError(_('User must have an email.'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = UserManager()

    def __str__(self):
        return self.email

