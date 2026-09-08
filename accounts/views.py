from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from .models import Address

def signup_view(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not first_name or not last_name or not username or not email or not phone or not password:
            return render(request, "signup.html", {
                "error": "Please fill all required fields."
            })

        if password != confirm_password:
            return render(request, "signup.html", {
                "error": "Passwords do not match."
            })

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {
                "error": "Username already exists."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "signup.html", {
                "error": "Email is already registered."
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        Profile.objects.create(
            user=user,
            phone=phone
        )

        auth_login(request, user)

        return redirect("home")

    return render(request, "signup.html")


def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:

            authenticated_user = authenticate(
                request,
                username=user.username,
                password=password
            )

            if authenticated_user is not None:

                auth_login(request, authenticated_user)

                return redirect("home")

        return render(request, "login.html", {
            "error": "Invalid email or password."
        })

    return render(request, "login.html")


def logout_view(request):

    logout(request)

    return redirect("home")

@login_required(login_url="/login/")
def profile_view(request):

    user = request.user

    # Create profile automatically if it does not exist
    profile, created = Profile.objects.get_or_create(
        user=user,
        defaults={
            "phone": ""
        }
    )

    addresses = user.addresses.all()

    if request.method == "POST":

        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()

        if not full_name or not email or not phone:
            messages.error(request, "Please fill all fields.")
            return redirect("profile")

        if User.objects.filter(
            email=email
        ).exclude(id=user.id).exists():

            messages.error(
                request,
                "This email is already registered."
            )

            return redirect("profile")

        # Split full name
        name_parts = full_name.split(" ", 1)

        user.first_name = name_parts[0]
        user.last_name = (
            name_parts[1]
            if len(name_parts) > 1
            else ""
        )

        user.email = email

        user.save()

        profile.phone = phone
        profile.save()

        messages.success(
            request,
            "Profile updated successfully!"
        )

        return redirect("profile")

    return render(
        request,
        "profile.html",
        {
            "user": user,
            "profile": profile,
            "addresses": addresses,
        }
    )

@login_required(login_url="/login/")
def add_address(request):

    if request.method != "POST":
        return redirect("profile")

    address_type = request.POST.get("address_type", "Home").strip()
    full_name = request.POST.get("full_name", "").strip()
    phone = request.POST.get("phone", "").strip()
    address = request.POST.get("address", "").strip()
    city = request.POST.get("city", "").strip()
    pincode = request.POST.get("pincode", "").strip()

    is_default = request.POST.get("is_default") == "on"

    # Validation
    if not full_name or not phone or not address or not city or not pincode:

        messages.error(
            request,
            "Please fill all address fields."
        )

        return redirect("profile")


    # If new address is default,
    # remove default from old addresses
    if is_default:

        Address.objects.filter(
            user=request.user
        ).update(
            is_default=False
        )


    # Create address
    Address.objects.create(

        user=request.user,

        address_type=address_type,

        full_name=full_name,

        phone=phone,

        address=address,

        city=city,

        pincode=pincode,

        is_default=is_default,
    )


    messages.success(
        request,
        "Address saved successfully!"
    )

    return redirect("profile")