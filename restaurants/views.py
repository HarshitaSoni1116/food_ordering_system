from django.shortcuts import render, get_object_or_404
from .models import Restaurant, FoodItem


def restaurant_list(request):

    restaurants = Restaurant.objects.filter(
        is_active=True
    ).order_by("-rating")

    return render(
        request,
        "restaurants.html",
        {
            "restaurants": restaurants
        }
    )


def restaurant_detail(request, restaurant_id):

    restaurant = get_object_or_404(
        Restaurant,
        id=restaurant_id,
        is_active=True
    )

    food_items = FoodItem.objects.filter(
        restaurant=restaurant,
        is_available=True
    ).order_by("-rating")

    return render(
        request,
        "restaurant-detail.html",
        {
            "restaurant": restaurant,
            "food_items": food_items
        }
    )


def menu(request):

    food_items = FoodItem.objects.filter(
        is_available=True,
        restaurant__is_active=True
    ).select_related(
        "restaurant"
    ).order_by("-rating")

    return render(
        request,
        "menu.html",
        {
            "food_items": food_items
        }
    )