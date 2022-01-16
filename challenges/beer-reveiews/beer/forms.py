from .models import Beer, BeerReview
from django.forms import ModelForm


class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['beer_name']


class BeerReviewForm(ModelForm):
    class Meta:
        model = BeerReview
        fields = ['review_body']
