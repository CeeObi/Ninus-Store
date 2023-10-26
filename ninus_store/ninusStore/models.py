from django.db import models
from django.contrib.auth.models import User


class Wishlist(models.Model):
    wish_name = models.CharField(max_length=255)
    wishlist_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.wish_name}"


# Create your models here.
class Collection(models.Model):
    col_name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.col_name}"


class Product(models.Model):
    COLOR_CHOICES = (
        ("BLACK", "Black"),
        ("WHITE", "White"),
        ("GRAY", "Gray"),
    )
    SIZE_CHOICES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    )
    TYPE_CHOICES = (
        ("H", "Hoodie"),
        ("C", "College"),
    )
    prod_name = models.CharField(max_length=255)
    img_url = models.CharField(max_length=2000)
    price = models.FloatField(max_length=255)
    color = models.CharField(max_length=9, choices=COLOR_CHOICES, default="BLACK")
    size = models.CharField(max_length=9, choices=SIZE_CHOICES, default="S")
    prod_type = models.CharField(max_length=9, choices=TYPE_CHOICES, default="H")
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    discount_amount = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.prod_name}"


class Order(models.Model):
    order_date = models.DateTimeField()
    order_name = models.CharField(max_length=255)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.order_name}"


class Purchase(models.Model):
    purchased_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return f"{self.purchased_item}"







