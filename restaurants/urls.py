from django.urls import path
from .views import (
    restaurant_list,
    restaurant_detail,
    menu,
)

urlpatterns = [

    path(
        "menu/",
        menu,
        name="menu"
    ),

    path(
        "",
        restaurant_list,
        name="restaurants"
    ),

    path(
        "<int:restaurant_id>/",
        restaurant_detail,
        name="restaurant_detail"
    ),

]