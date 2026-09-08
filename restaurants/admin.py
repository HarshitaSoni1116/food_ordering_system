from django.contrib import admin
from .models import Restaurant, FoodItem


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "city",
        "cuisine_type",
        "rating",
        "delivery_time",
        "is_open",
        "is_active",
    )

    list_filter = (
        "cuisine_type",
        "is_open",
        "is_active",
    )

    search_fields = (
        "name",
        "city",
        "address",
    )


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "restaurant",
        "category",
        "price",
        "is_vegetarian",
        "is_available",
    )

    list_filter = (
        "category",
        "is_vegetarian",
        "is_available",
    )

    search_fields = (
        "name",
        "restaurant__name",
    )