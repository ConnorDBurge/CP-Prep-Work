from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    body = models.TextField(max_length=250)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)