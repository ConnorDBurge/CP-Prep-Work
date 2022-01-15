from http.client import HTTPResponse
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
            return HTTPResponse('Oops! Something went wrong')
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
            return HTTPResponse('Oops! Something went wrong')
    else:
        form = BrandForm(instance=brand)
        return render(request, 'brand/brand_form.html', {'form': form, 'type': 'Edit'})


def car_new(request, brand_id):
    brand = get_brand(brand_id)
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.car_brand = brand
            car.save()
            return redirect('brand_detail', brand_id=brand.id)
        else:
            return HTTPResponse('Oops! Something went wrong')
    else:
        form = CarForm()
        return render(request, 'car/car_form.html', {'form': form, 'brand': brand, 'type': 'New'})


def car_detail(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    return render(request, 'car/car_detail.html', {'brand': brand, 'car': car})


def car_edit(request, brand_id, car_id):
    brand = get_brand(brand_id)
    car = get_car(car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.car_brand = brand
            car.save()
            return redirect('brand_detail', brand_id=brand.id)
        else:
            return HTTPResponse('Oops! Something went wrong')
    else:
        form = CarForm(instance=car)
        return render(request, 'car/car_form.html', {'form': form, 'brand': brand, 'type': 'Edit'})
