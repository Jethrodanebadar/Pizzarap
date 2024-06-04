from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/main", views.main, name="main-page"),
    path("home/main/cart", views.add_to_cart, name="cart"),
    path("home/main/user/cart", views.cartDisplay, name="cart_display"),
    path("home/main/user/delete/<int:item_id>", views.delete_item, name="delete-item"),
    path("home/main/user/cart/clear", views.empty_cart, name="empty_cart"),
    path("home/main/login", views.LoginInterfaceView.as_view(), name="login"),
    path("home/main/login/signup", views.SignupView.as_view(), name="signup"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout")
]