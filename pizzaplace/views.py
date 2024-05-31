import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import pizza_detail, Appetizer, Salad, Drink, Cart, CartItem
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    user = request.user
    user_name = user.username
    return render(request, "pizzaplace/home.html", {
    "username": user_name
    })

def main(request):
    pizza_details = pizza_detail.objects.all()
    appetizer = Appetizer.objects.all()
    salad = Salad.objects.all()
    drink = Drink.objects.all()
    return render(request, "pizzaplace/main.html", {
        "pizzas": pizza_details,
        "appetizers": appetizer,
        "salads": salad,
        "drinks": drink,
        # "cart_items": request.user.cart.items.all().count()
    })

class LoginInterfaceView(LoginView):
    template_name = "pizzaplace/login.html"

class LogoutInterfaceView(LogoutView):
    template_name = "pizzaplace/logout.html"

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'pizzaplace/signup.html'
    success_url = '/home/'

@login_required()
def cartDisplay(request):
    return render(request, "pizzaplace/cart.html")


# def add_to_cart(request):
#     pass
#     # submit form
#     # find Cart
#         # give user cart if they don't have one
#     # add items to cart
#     # redirect back to main