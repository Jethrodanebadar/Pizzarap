from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Pizza(models.Model):
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




class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user}"


class CartItem(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    item_type = models.CharField(max_length=50)
    item_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='medium')

    def __str__(self):
        item = self.get_item()
        if self.item_type == "Pizza":
            return f"{item.pizza_name} - {self.size}"
        else:
            return item.name

    def get_item(self):
        if self.item_type == "Salad":
            item = Salad.objects.get(pk=self.item_id)
        elif self.item_type == "Pizza":
            item = Pizza.objects.get(pk=self.item_id)
        elif self.item_type == "Drink":
            item = Drink.objects.get(pk=self.item_id)
        elif self.item_type == "Appetizer":
            item = Appetizer.objects.get(pk=self.item_id)
        else:
            raise ValueError(f"Invalid item_type ({self.item_type})")
        return item

    def get_price(self):
        item = self.get_item()
        if self.item_type == "Pizza":
            if self.size == "small":
                return item.small_price * self.quantity
            elif self.size == "medium":
                return item.medium_price * self.quantity
            elif self.size == "large":
                return item.large_price * self.quantity
            else:
                raise ValueError("Invalid pizza size")
        else:
            return item.price * self.quantity

