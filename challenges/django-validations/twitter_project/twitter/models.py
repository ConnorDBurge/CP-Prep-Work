from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import *


def validate_age(age):
    if age < 13:
        raise ValidationError('Age must be at least 13')


def validate_account(type):
    valid_types = ['free', 'paid']
    if type not in valid_types:
        raise ValidationError(f'Invalid account type for {type}')


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(13)])
    account_type = models.CharField(
        max_length=4, validators=[validate_account])
