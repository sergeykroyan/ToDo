from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user.views import UserRegistrationAPI, UserUpdateAPI

app_name = 'user'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserRegistrationAPI.as_view(), name='user-register'),
    path('update/<int:pk>/', UserUpdateAPI.as_view(), name='user-update'),
]
