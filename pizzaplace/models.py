from django.db import models

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