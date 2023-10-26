from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Collections(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    order_date = models.DateTimeField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    price=models.FloatField(max_length=255)
    quantity = models.IntegerField()



