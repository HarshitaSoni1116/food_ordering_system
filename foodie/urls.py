from django.contrib import admin
from django.urls import path
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def restaurants(request):
    return render(request, "restaurants.html")


def menu(request):
    return render(request, "menu.html")


def offers(request):
    return render(request, "offers.html")


def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")


def admin_login(request):
    return render(request, "admin-login.html")

def signup(request):
    return render(request, "signup.html")


def forgot_password(request):
    return render(request, "forgot-password.html")


def reset_password(request):
    return render(request, "reset-password.html")

def restaurant_detail(request, restaurant_id):
    return render(request, "restaurant-detail.html", {
        "restaurant_id": restaurant_id
    })

def food_detail(request, food_id):
    return render(request, "food-detail.html", {
        "food_id": food_id
    })

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def order_confirmation(request):
    return render(request, "order-confirmation.html")

def profile(request):
    return render(request, "profile.html")

def my_orders(request):
    return render(request, "my-orders.html")

def owner_dashboard(request):
    return render(request, "owner-dashboard.html")

def admin_dashboard(request):
    return render(request, "admin-dashboard.html")

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("restaurants/", restaurants, name="restaurants"),
    path("menu/", menu, name="menu"),
    path("offers/", offers, name="offers"),
    path("about/", about, name="about"),
    path("login/", login, name="login"),
    path("admin-login/", admin_login, name="admin_login"),
    path("signup/", signup, name="signup"),
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password/", reset_password, name="reset_password"),
    path("restaurant/<int:restaurant_id>/", restaurant_detail , name="restaurant_detail"),
    path("food/<int:food_id>/",food_detail,name="food_detail"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("order-confirmation/",order_confirmation,name="order_confirmation"),
    path("profile/", profile, name="profile"),
    path("my-orders/", my_orders, name="my_orders"),
    path("owner/dashboard/", owner_dashboard, name="owner_dashboard"),
    path("foodie-admin/dashboard/", admin_dashboard, name="admin_dashboard"),
]