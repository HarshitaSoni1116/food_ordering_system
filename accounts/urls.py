from django.urls import path
from .views import (
    signup_view,
    login_view,
    logout_view,
    add_address,
    edit_address,
    delete_address,
    forgot_password,
    profile_view,
)
from .views import reset_password


urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
    "add-address/",
    add_address,
    name="add_address"
),
path(
    "address/<int:address_id>/edit/",
    edit_address,
    name="edit_address"
),

path(
    "address/<int:address_id>/delete/",
    delete_address,
    name="delete_address"
),
path("reset-password/", reset_password, name="reset_password"),

path("forgot-password/", forgot_password, name="forgot_password"),
]