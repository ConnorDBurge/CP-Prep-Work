from django.db import models


# And finally if you have set up your associations correctly a user should have many food items through orders. See the final test.

class User(models.Model):
    pass


class Restaurant(models.Model):
    pass


class FoodItem(models.Model):
    orders = models.ManyToManyField(
        'Order', related_name='food_items', through='OrderFoodItem')


class Order(models.Model):
    # A user has many orders -- user.orders
    # An order belongs to a user -- order.user
    user = models.ForeignKey(
        User, related_name="orders", on_delete=models.CASCADE)
    # A restaurant has many orders
    # An order belongs to a restaurant
    restaurant = models.ForeignKey(
        Restaurant, related_name="orders", on_delete=models.CASCADE)


class OrderFoodItem(models.Model):
    # An order has many order_food_items
    # An order_food_item belongs to an order
    order = models.ForeignKey(
        Order, related_name="order_food_items", on_delete=models.CASCADE)
    # A food item has many order_food_items
    # An order_food_item belongs to a food_item
    food_item = models.ForeignKey(
        FoodItem, related_name="order_food_items", on_delete=models.CASCADE)
