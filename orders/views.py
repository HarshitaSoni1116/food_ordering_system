import json
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from .models import Order, OrderItem
from restaurants.models import FoodItem


@login_required(login_url="/login/")
def place_order(request):

    if request.method != "POST":
        return redirect("checkout")

    # -----------------------------
    # Customer Details
    # -----------------------------

    customer_name = request.POST.get("fullName", "").strip()
    phone = request.POST.get("phone", "").strip()
    address = request.POST.get("address", "").strip()
    city = request.POST.get("city", "").strip()
    pincode = request.POST.get("pincode", "").strip()
    instructions = request.POST.get("instructions", "").strip()

    payment_method = request.POST.get(
        "payment",
        "cod"
    )

    # -----------------------------
    # Validate Customer Details
    # -----------------------------

    if not customer_name or not phone or not address or not city or not pincode:

        return render(
            request,
            "checkout.html",
            {
                "user": request.user,
                "profile": request.user.profile,
                "error": "Please fill all required delivery details."
            }
        )

    # -----------------------------
    # Get Real Cart
    # -----------------------------

    cart_data = request.POST.get(
        "cart_data",
        "[]"
    )

    try:
        cart_items = json.loads(cart_data)
    except json.JSONDecodeError:

        return render(
            request,
            "checkout.html",
            {
                "user": request.user,
                "profile": request.user.profile,
                "error": "Invalid cart data."
            }
        )

    # -----------------------------
    # Empty Cart Check
    # -----------------------------

    if not cart_items:

        return render(
            request,
            "checkout.html",
            {
                "user": request.user,
                "profile": request.user.profile,
                "error": "Your cart is empty."
            }
        )

    # -----------------------------
    # Create Order
    # -----------------------------

    with transaction.atomic():

        order = Order.objects.create(

            user=request.user,

            customer_name=customer_name,

            phone=phone,

            email=request.user.email,

            address=address,

            city=city,

            pincode=pincode,

            delivery_instructions=instructions,

            delivery_fee=Decimal("40.00"),

            status="Pending",

            payment_status="Pending",

            payment_method=(
                "Cash on Delivery"
                if payment_method == "cod"
                else "Online Payment"
            ),
        )

        subtotal = Decimal("0.00")

        # -----------------------------
        # Create Order Items
        # -----------------------------

        for cart_item in cart_items:

            food_id = cart_item.get("id")
            quantity = int(
                cart_item.get("quantity", 1)
            )

            if not food_id or quantity < 1:
                continue

            food = FoodItem.objects.get(
                id=food_id,
                is_available=True
            )

            item_subtotal = (
                food.price * quantity
            )

            OrderItem.objects.create(

                order=order,

                food_item=food,

                food_name=food.name,

                price=food.price,

                quantity=quantity,

                subtotal=item_subtotal,
            )

            subtotal += item_subtotal

        # -----------------------------
        # Calculate Total
        # -----------------------------

        order.total_amount = (
            subtotal + order.delivery_fee
        )

        order.save()

    # -----------------------------
    # Order Successful
    # -----------------------------

    return redirect("order_confirmation")