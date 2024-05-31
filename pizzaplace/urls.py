from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/main", views.main, name="main-page"),
    path("home/main/cart", views.cartDisplay, name="cart"),
    # path("home/main/addtocart", views.add_to_cart, name="add_to_cart"),
    path("home/main/login", views.LoginInterfaceView.as_view(), name="login"),
    path("home/main/login/signup", views.SignupView.as_view(), name="signup"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout")
]