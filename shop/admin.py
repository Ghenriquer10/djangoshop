from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Redefina os fieldsets sem os campos 'groups' e 'user_permissions'
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Informações Pessoais",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "address",
                    "is_administrator",
                )
            },
        ),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )

    # Redefina add_fieldsets para adicionar novos usuários
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "phone",
                    "address",
                    "is_administrator",
                ),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "phone",
        "address",
        "is_staff",
        "is_administrator",
    )
    search_fields = ("email", "username", "phone")


# Registra o modelo de usuário personalizado com a classe de administração personalizada
admin.site.register(CustomUser, CustomUserAdmin)
