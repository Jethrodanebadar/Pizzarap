from django.contrib import admin
from . import models
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ("pizza_name",)

class AppetizerAdmin(admin.ModelAdmin):
    list_display = ("name",)

class SaladAdmin(admin.ModelAdmin):
    list_display = ("name",)

class DrinkAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.Salad, SaladAdmin)
admin.site.register(models.pizza_detail, PizzaAdmin)
admin.site.register(models.Appetizer, AppetizerAdmin)
admin.site.register(models.Drink, DrinkAdmin)