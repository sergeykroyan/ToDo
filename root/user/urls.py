from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from user.views import UserCreateAPI

urlpatterns = [
    path('register/', UserCreateAPI.as_view(), name='user-list'),
]
