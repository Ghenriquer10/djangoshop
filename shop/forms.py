from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "address", "password1", "password2")
        labels = {
            "username": "Nome de usuário",
            "email": "E-mail",
            "phone": "Telefone",
            "address": "Endereço",
            "password1": "Senha",
            "password2": "Confirme a senha",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Nome de usuário"}),
            "email": forms.EmailInput(attrs={"placeholder": "E-mail"}),
            "phone": forms.TextInput(attrs={"placeholder": "Telefone"}),
            "address": forms.TextInput(attrs={"placeholder": "Endereço"}),
            "password1": forms.PasswordInput(attrs={"placeholder": "Senha"}),
            "password2": forms.PasswordInput(attrs={"placeholder": "Confirme a senha"}),
        }
        help_texts = {
            "username": None,
        }
        error_messages = {
            "username": {
                "unique": "Este nome de usuário já está em uso.",
            },
        }
