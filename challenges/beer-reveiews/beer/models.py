from django.db import models
from django.conf import settings


class Beer(models.Model):
    beer_name = models.CharField(max_length=200)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.beer_name
