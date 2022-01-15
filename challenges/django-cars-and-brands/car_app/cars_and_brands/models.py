from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    car_model = models.CharField(max_length=200)
    car_brand = models.ForeignKey(
        Brand, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_brand}: {self.car_model}'
