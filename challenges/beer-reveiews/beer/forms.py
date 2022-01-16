from .models import Beer
from django.forms import ModelForm


class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['beer_name']
