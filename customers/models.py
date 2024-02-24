from django.db import models
from companies.models import Product

# Create your models here.

class Customer(models.Model):                   # ПОКУПАТЕЛИ
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    product = models.ManyToManyField(Product)    # Многие ко многим

    class Meta:
        ordering = ['fist_name']


class SuggestionsForImrovement(models.Model):  # ПРЕДЛОЖЕНИЯ ПО УЛУЧШЕНИЮ РАБОТЫ
    comment = models.TextField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)  # ForeignKey


class Review(models.Model):                 # Отзывы о товаре
    comment = models.TextField(null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  # ForeignKey


class Order(models.Model):                  # ЗАКАЗЫ
    created_at = models.DateTimeField(auto_now_add=True)
    # order_count = models.IntegerField(max_length=200) # (с METANIT - хранит количество купленного товара)

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)  # ForeignKey
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  # ForeignKey
