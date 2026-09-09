from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from .models import Address
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

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

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        authenticated_user = authenticate(
            request,
            username=username,
            password=password
        )

        if authenticated_user is not None:

            auth_login(request, authenticated_user)

            return redirect("home")

        return render(request, "login.html", {
            "error": "Invalid username or password."
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

@login_required(login_url="/login/")
def edit_address(request, address_id):

    address = Address.objects.filter(
        id=address_id,
        user=request.user
    ).first()

    if not address:
        messages.error(request, "Address not found.")
        return redirect("profile")

    if request.method == "POST":

        address.address_type = request.POST.get(
            "address_type", "Home"
        ).strip()

        address.full_name = request.POST.get(
            "full_name", ""
        ).strip()

        address.phone = request.POST.get(
            "phone", ""
        ).strip()

        address.address = request.POST.get(
            "address", ""
        ).strip()

        address.city = request.POST.get(
            "city", ""
        ).strip()

        address.pincode = request.POST.get(
            "pincode", ""
        ).strip()

        is_default = request.POST.get("is_default") == "on"

        if is_default:
            Address.objects.filter(
                user=request.user
            ).exclude(
                id=address.id
            ).update(
                is_default=False
            )

        address.is_default = is_default
        address.save()

        messages.success(
            request,
            "Address updated successfully!"
        )

        return redirect("profile")

    return render(
        request,
        "edit_address.html",
        {
            "address": address
        }
    )

@login_required(login_url="/login/")
def delete_address(request, address_id):

    address = Address.objects.filter(
        id=address_id,
        user=request.user
    ).first()

    if not address:
        messages.error(request, "Address not found.")
        return redirect("profile")

    if request.method == "POST":

        address.delete()

        messages.success(
            request,
            "Address deleted successfully!"
        )

    return redirect("profile")

def forgot_password(request):

    if request.method == "POST":
        email = request.POST.get("email", "").strip()

        user = User.objects.filter(email=email).first()

        if user:
            token = default_token_generator.make_token(user)

            reset_url = request.build_absolute_uri(
                reverse("reset_password")
            ) + f"?uid={user.pk}&token={token}"

            send_mail(
                subject="Foodie - Password Reset",
                message=f"""
Hello {user.username},

We received a request to reset your Foodie account password.

Click the link below to reset your password:

{reset_url}

If you did not request this, you can safely ignore this email.

Regards,
Foodie Team
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

        # Same message whether email exists or not
        messages.success(
            request,
            "If an account exists with this email, a password reset link has been sent."
        )

        return redirect("forgot_password")

    return render(request, "forgot-password.html")

def reset_password(request):

    uid = request.GET.get("uid")
    token = request.GET.get("token")

    if not uid or not token:
        messages.error(request, "Invalid or expired reset link.")
        return redirect("forgot_password")

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        messages.error(request, "Invalid or expired reset link.")
        return redirect("forgot_password")

    # Check token
    if not default_token_generator.check_token(user, token):
        messages.error(request, "This reset link is invalid or has expired.")
        return redirect("forgot_password")

    if request.method == "POST":
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if len(password) < 8:
            return render(request, "reset-password.html", {
                "error": "Password must be at least 8 characters long."
            })

        if password != confirm_password:
            return render(request, "reset-password.html", {
                "error": "Passwords do not match."
            })

        user.set_password(password)
        user.save()

        messages.success(
            request,
            "Password reset successfully. You can now login."
        )

        return redirect("login")

    return render(request, "reset-password.html")