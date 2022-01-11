# Generated by Django 3.2.4 on 2022-01-11 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodDelivery', '0003_remove_fooditem_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='orders',
            field=models.ManyToManyField(related_name='food_items', to='foodDelivery.Order'),
        ),
    ]
