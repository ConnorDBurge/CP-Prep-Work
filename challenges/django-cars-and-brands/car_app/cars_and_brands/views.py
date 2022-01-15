from django.shortcuts import render, redirect
from .models import Car, Brand
from .forms import CarForm, BrandForm


def get_car(car_id):
    return Car.objects.get(id=car_id)


def get_brand(brand_id):
    return Brand.objects.get(id=brand_id)


def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brand/brand_list.html', {'brands': brands})


def brand_new(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm()
        return render(request, 'brand/brand_form.html', {'form': form, 'type': 'New'})


def brand_detail(request, brand_id):
    brand = get_brand(brand_id)
    cars = brand.cars.all().order_by('car_model')
    return render(request, 'brand/brand_detail.html', {'cars': cars, 'brand': brand})


def brand_edit(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            return redirect('brand_detail', brand_id=brand.id)
    else:
        form = BrandForm(instance=brand)
        return render(request, 'brand/brand_form.html', {'form': form, 'type': 'Edit'})


def car_list(request, brand_id):
    pass


def car_new(request, brand_id):
    pass


def car_detail(request, brand_id, car_id):
    pass


def car_edit(request, brand_id, car_id):
    pass
