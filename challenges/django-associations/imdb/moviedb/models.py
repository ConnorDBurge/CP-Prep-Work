from django.db import models


class Actor(models.Model):
    pass


class Movie(models.Model):
    actors = models.ManyToManyField(
        Actor, related_name='movies', through='Role')


class Role(models.Model):
    actor = models.ForeignKey(
        Actor, related_name='roles', on_delete=models.CASCADE)
    movie = models.ForeignKey(
        Movie, related_name='roles', on_delete=models.CASCADE)
