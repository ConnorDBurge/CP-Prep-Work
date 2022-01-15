from .models import Car, Brand
from django.forms import ModelForm


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['car_model']


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']
