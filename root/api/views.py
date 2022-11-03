from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from todo.models import Task
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser


class TaskUserWritePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class TaskList(generics.ListCreateAPIView):
    permission_classes = [TaskUserWritePermission]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [TaskUserWritePermission]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
