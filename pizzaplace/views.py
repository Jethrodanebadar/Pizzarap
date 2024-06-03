from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Pizza, Appetizer, Salad, Drink, CartItem, Cart
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import AddToCartForm


# Create your views here.

def home(request):
    user = request.user
    user_name = user.username
    return render(request, "pizzaplace/home.html", {
        "username": user_name
    })


def main(request):
    pizza_details = Pizza.objects.all()
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


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            form.create_items_from_form(request.user)
            return JsonResponse({
                "response": "success"
            })
        else:
            pass
    else:
        return JsonResponse({
            "response": "Failed to add item on this cart"
        })


@login_required(login_url="/home/main/login/")
def cartDisplay(request):
    cart_items = request.user.cart.items.all()
    username = request.user.username
    context = {
        'username': username,
        'cart_items': cart_items
    }
    return render(request, 'pizzaplace/cart.html', context)