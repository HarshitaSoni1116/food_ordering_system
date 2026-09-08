from django.urls import path
from .views import (
    signup_view,
    login_view,
    logout_view,
    add_address,
)


urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
    "add-address/",
    add_address,
    name="add_address"
),
]