from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone", "address")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone", "address")}),
    )
    list_display = ("username", "email", "phone", "address", "is_staff")
    search_fields = ("email", "username", "phone")


admin.site.register(CustomUser, CustomUserAdmin)
