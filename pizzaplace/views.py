from django.contrib.admin.utils import get_deleted_objects
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
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

    def form_valid(self, form):
        response = super().form_valid(form)
        if not Cart.objects.filter(user=self.request.user).exists():
            Cart.objects.create(user=self.request.user)
        return response

class LogoutInterfaceView(LogoutView):
    template_name = "pizzaplace/logout.html"



class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'pizzaplace/signup.html'
    success_url = '/home/'

    def form_valid(self, form):
        response = super().form_valid(form)
        Cart.objects.create(user=self.object)
        return response

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
       return JsonResponse({"response": "error"})


@login_required(login_url="/home/main/login/")
def cartDisplay(request):
    try:
        cart = request.user.cart
        cart_items = cart.items.all()
        item_count = cart_items.count()
        cartisempty = item_count == 0

        total_price = sum(item.get_price() for item in cart_items)
    except Cart.DoesNotExist:
        item_count = 0
        cartisempty = True
        cart_items = []

    username = request.user.username
    context = {
        'username': username,
        'cart_items': cart_items,
        'isEmpty': cartisempty,
        "total": total_price
    }
    return render(request, 'pizzaplace/cart.html', context)

def delete_item(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    return redirect('cart_display')


def empty_cart(request):
    CartItem.objects.all().delete()
    return render(request, "pizzaplace/emptycart.html")