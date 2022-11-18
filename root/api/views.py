from rest_framework import generics
from .serializers import TaskSerializer
from todo.models import Task
from .permissions import TaskUserWritePermission


class TaskList(generics.ListCreateAPIView):
    permission_classes = [TaskUserWritePermission]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [TaskUserWritePermission]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.id)
