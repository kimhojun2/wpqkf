from django.db import models
from django.conf import settings
# Create your models here.

class Board(models.Model):
    user_seq = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=8000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class Comment(models.Model):
    user_seq = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    board_seq = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    level = models.SmallIntegerField()
    group = models.SmallIntegerField()
    order = models.SmallIntegerField()
    parent = models.IntegerField()
