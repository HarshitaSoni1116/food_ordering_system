from django.contrib import admin
from .models import Profile, Address


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone",
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "user",
        "address_type",
        "city",
        "pincode",
        "is_default",
    )

    list_filter = (
        "address_type",
        "city",
        "is_default",
    )

    search_fields = (
        "full_name",
        "phone",
        "city",
        "pincode",
        "user__username",
    )