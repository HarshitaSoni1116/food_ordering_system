from django.db import models


class Restaurant(models.Model):
    CUISINE_CHOICES = [
        ("North Indian", "North Indian"),
        ("South Indian", "South Indian"),
        ("Chinese", "Chinese"),
        ("Italian", "Italian"),
        ("Fast Food", "Fast Food"),
        ("Multi Cuisine", "Multi Cuisine"),
    ]

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    address = models.TextField()
    city = models.CharField(max_length=100)

    cuisine_type = models.CharField(
        max_length=50,
        choices=CUISINE_CHOICES,
        default="Multi Cuisine"
    )

    image = models.ImageField(
        upload_to="restaurants/",
        blank=True,
        null=True
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0
    )

    delivery_time = models.PositiveIntegerField(
        default=30,
        help_text="Delivery time in minutes"
    )

    delivery_fee = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=40.00
    )

    is_open = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class FoodItem(models.Model):
    CATEGORY_CHOICES = [
        ("Starters", "Starters"),
        ("Main Course", "Main Course"),
        ("Pizza", "Pizza"),
        ("Burger", "Burger"),
        ("Rice", "Rice"),
        ("Pasta", "Pasta"),
        ("Desserts", "Desserts"),
        ("Beverages", "Beverages"),
    ]

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="food_items"
    )

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to="food/",
        blank=True,
        null=True
    )

    is_vegetarian = models.BooleanField(default=True)
    is_available = models.BooleanField(default=True)

    preparation_time = models.PositiveIntegerField(
        default=20,
        help_text="Preparation time in minutes"
    )

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"