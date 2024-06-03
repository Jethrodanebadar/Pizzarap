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


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("get_username", "item_type", 'get_item_name', "quantity")

    def get_username(self, obj):
        return obj.cart.user.username

    def get_item_name(self, obj):
        return str(obj)


admin.site.register(models.Salad, SaladAdmin)
admin.site.register(models.Pizza, PizzaAdmin)
admin.site.register(models.Appetizer, AppetizerAdmin)
admin.site.register(models.Drink, DrinkAdmin)
admin.site.register(models.CartItem, CartItemAdmin)
