from django.db import models
from django.conf import settings


class Beer(models.Model):
    beer_name = models.CharField(max_length=200)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.beer_name


class BeerReview(models.Model):
    review_body = models.TextField()
    beer_name = models.ForeignKey(
        Beer, on_delete=models.CASCADE, related_name='reviews')
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'Review for {self.beer_name} submitted by {self.added_by}'
