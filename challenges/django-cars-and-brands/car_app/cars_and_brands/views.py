from django.shortcuts import render, redirect
from .models import Car, Brand
from .forms import CarForm, BrandForm


def brand_list(request):
    pass


def brand_new(request):
    pass


def brand_detail(request, brand_id):
    pass


def brand_edit(request, brand_id):
    pass


def car_list(request, brand_id):
    pass


def car_new(request, brand_id):
    pass


def car_detail(request, brand_id, car_id):
    pass


def car_edit(request, brand_id, car_id):
    pass
