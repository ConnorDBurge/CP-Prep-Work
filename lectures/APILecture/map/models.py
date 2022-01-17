from django.db import models


class Landmark(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'ID: {self.id} - {self.name} is located at {self.address}'
