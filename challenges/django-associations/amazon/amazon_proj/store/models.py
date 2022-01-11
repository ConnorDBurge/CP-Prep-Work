from django.db import models


class User(models.Model):
    # user.shop
    # user.reviewed_products
    pass


class Shop(models.Model):
    # shop.owner
    owner = models.ForeignKey(
        User, related_name="shop", on_delete=models.CASCADE)
    # shop.products


class Product(models.Model):
    # product.shop
    shop = models.ForeignKey(
        Shop, related_name="products", on_delete=models.CASCADE)
    # product.reviews


class Review(models.Model):
    # review.product
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE)
    # review.user
    user = models.ForeignKey(
        User, related_name="reviewed_products", on_delete=models.CASCADE)
