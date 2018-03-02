from django.db import models
from users.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True, blank=True, null=True)
    user = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE, null=False)
    body = models.TextField()

    class Meta:
        ordering = ('created',)
