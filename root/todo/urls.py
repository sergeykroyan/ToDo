from django.urls import path
from .views import *

app_name = 'todo'

urlpatterns = [
    path('', app, name='tasks'),
]