from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Informações do SaaS", {
            "fields": ("tenant", "role"),
        }),
    )

    list_display = (
        "username",
        "email",
        "tenant",
        "role",
        "is_staff",
        "is_active",
    )

    list_filter = ("role", "tenant")
