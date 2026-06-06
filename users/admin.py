from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "email", "phone_number", "is_staff", "is_superuser"]

    fieldsets = UserAdmin.fieldsets + (
        ("اطلاعات تکمیلی", {"fields": ("phone_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("اطلاعات تکمیلی", {"fields": ("phone_number",)}),
    )