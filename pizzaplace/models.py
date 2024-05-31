from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class pizza_detail(models.Model):
    pizza_name = models.CharField(max_length=50, blank=False)
    pizza_description = models.TextField()
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    medium_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.pizza_name


class Appetizer(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


# class Item(models.Model):
#     TypeChoices = (
#         ("Drink", "Drink"),
#         ("Pizza", "Pizza"),
#         ("Salad", "Salad"),
#         ("Appetizer", "Appetizer"),
#     )
#
#     name
#     item_type = models.CharField(choices=TypeChoices)
#     description
#     price


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    item_type = models.CharField(max_length=50)
    item_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item_name}"

    def get_item(self):
        if self.item_type == "Salad":
            item = Salad.objects.get(pk=self.item_id)
        elif self.item_type == "Salad":
            item = Salad.objects.get(pk=self.item_id)
        elif self.item_type == "Salad":
            item = Salad.objects.get(pk=self.item_id)

    def get_price(self):
        return self.get_item().price * self.quantity
