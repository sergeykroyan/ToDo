from django.urls import path
from user.views import UserCreateAPI, UserUpdateAPI

app_name = 'user'

urlpatterns = [
    path('register/', UserCreateAPI.as_view(), name='user-register'),
    path('update/<int:pk>/', UserUpdateAPI.as_view(), name='user-update'),
]
