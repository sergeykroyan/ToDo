from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


def app(request):
    return HttpResponse('hi')
