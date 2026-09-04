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
]