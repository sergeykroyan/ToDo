from django.db import models
import jwt
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractBaseUser,\
    PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if username is None:
            raise ValueError('User must have a username.')
        if email is None:
            raise ValueError('User must have an email.')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise ValueError('Superuser must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_stuff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    object = UserManager()

    def __str__(self):
        return self.email

