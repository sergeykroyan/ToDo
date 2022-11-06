from django.db import models
from django.conf import settings
from user.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=99)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete', 'created']
