from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from restaurants.models import Restaurant, FoodItem
from orders.models import Order
from accounts.views import profile_view

# =========================
# HOME
# =========================

def home(request):
    return render(request, "home.html")


# =========================
# RESTAURANTS
# =========================

def restaurants(request):
    restaurant_list = Restaurant.objects.filter(
        is_active=True
    ).order_by("-rating")

    return render(request, "restaurants.html", {
        "restaurants": restaurant_list
    })


def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(
        Restaurant,
        id=restaurant_id,
        is_active=True
    )

    food_items = restaurant.food_items.filter(
        is_available=True
    )

    return render(request, "restaurant-detail.html", {
        "restaurant": restaurant,
        "food_items": food_items,
    })


# =========================
# FOOD
# =========================

def food_detail(request, food_id):
    food = get_object_or_404(
        FoodItem,
        id=food_id,
        is_available=True
    )

    return render(request, "food-detail.html", {
        "food": food
    })


# =========================
# OTHER PAGES
# =========================

def menu(request):
    return render(request, "menu.html")


def offers(request):
    return render(request, "offers.html")


def about(request):
    return render(request, "about.html")


def admin_login(request):
    return render(request, "admin-login.html")


def forgot_password(request):
    return render(request, "forgot-password.html")


def reset_password(request):
    return render(request, "reset-password.html")


def cart(request):
    return render(request, "cart.html")


@login_required(login_url="/login/")
def checkout(request):
    return render(request, "checkout.html", {
        "user": request.user,
        "profile": request.user.profile,
    })


@login_required(login_url="/login/")
def order_confirmation(request):
    order = (
        request.user.orders
        .prefetch_related("items__food_item")
        .order_by("-created_at")
        .first()
    )

    if not order:
        return redirect("home")

    subtotal = sum(
        item.subtotal for item in order.items.all()
    )

    return render(
        request,
        "order-confirmation.html",
        {
            "order": order,
            "items": order.items.all(),
            "subtotal": subtotal,
        }
    )


@login_required(login_url="/login/")
def profile(request):
    return render(request, "profile.html", {
        "user": request.user,
        "profile": request.user.profile,
    })

@login_required(login_url="/login/")
def my_orders(request):

    orders = request.user.orders.prefetch_related(
        "items"
    ).order_by("-created_at")

    total_orders = orders.count()

    active_orders = orders.exclude(
        status__in=["Delivered", "Cancelled"]
    ).count()

    delivered_orders = orders.filter(
        status="Delivered"
    ).count()

    total_spent = sum(
        order.total_amount for order in orders
        if order.payment_status == "Paid"
    )

    return render(request, "my-orders.html", {
        "orders": orders,
        "total_orders": total_orders,
        "active_orders": active_orders,
        "delivered_orders": delivered_orders,
        "total_spent": total_spent,
    })

@login_required(login_url="/login/")
def order_details(request, order_id):
    order = get_object_or_404(
        Order.objects.prefetch_related("items__food_item"),
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "order-details.html",
        {
            "order": order,
            "items": order.items.all(),
        }
    )

@login_required(login_url="/login/")
def track_order(request, order_id):
    order = get_object_or_404(
        Order.objects.prefetch_related("items"),
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "track-order.html",
        {
            "order": order,
        }
    )

def owner_dashboard(request):
    return render(request, "owner-dashboard.html")


def admin_dashboard(request):
    return render(request, "admin-dashboard.html")


# =========================
# URL PATTERNS
# =========================

urlpatterns = [

    # Django Admin
    path("admin/", admin.site.urls),

    # Accounts
    path("", include("accounts.urls")),

    # Orders
    path("", include("orders.urls")),

    # Home
    path("", home, name="home"),

    # Restaurants
    path("restaurants/", restaurants, name="restaurants"),
    path(
        "restaurant/<int:restaurant_id>/",
        restaurant_detail,
        name="restaurant_detail"
    ),

    # Food
    path(
        "food/<int:food_id>/",
        food_detail,
        name="food_detail"
    ),

    # Other pages
    path("menu/", menu, name="menu"),
    path("offers/", offers, name="offers"),
    path("about/", about, name="about"),
    path("admin-login/", admin_login, name="admin_login"),

    # Admin/Owner
    path(
        "foodie-admin/dashboard/",
        admin_dashboard,
        name="admin_dashboard"
    ),
    path(
        "owner/dashboard/",
        owner_dashboard,
        name="owner_dashboard"
    ),

    # Orders
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path(
        "order-confirmation/",
        order_confirmation,
        name="order_confirmation"
    ),

    # User
    path("profile/", profile_view, name="profile"),
    path("my-orders/", my_orders, name="my_orders"),

    # Password
    path(
        "forgot-password/",
        forgot_password,
        name="forgot_password"
    ),
    path(
        "reset-password/",
        reset_password,
        name="reset_password"
    ),
    path(
    "order/<int:order_id>/",
    order_details,
    name="order_details"
    ),
    path(
    "order/<int:order_id>/track/",
    track_order,
    name="track_order"
),
]