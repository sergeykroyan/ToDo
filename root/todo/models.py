from django.db import models
from django.conf import settings


class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=99)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete', 'created']
