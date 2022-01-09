# Generated by Django 2.1.5 on 2022-01-09 20:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_auto_20220109_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(13)]),
        ),
    ]
