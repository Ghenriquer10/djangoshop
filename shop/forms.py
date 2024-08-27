from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    # Altera implicitamente os nomes dos campos de login e senha
    class Meta:
        model = CustomUser
        fields = ("username", "password")
        labels = {
            "username": "Nome de usuário",
            "password": "Senha",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={"placeholder": "Nome de usuário", "class": "form-control"}
            ),
            "password": forms.PasswordInput(
                attrs={"placeholder": "Senha", "class": "form-control"}
            ),
        }
        help_texts = {
            "username": None,
            "password": None,
        }

        error_messages = {
            "username": {
                "invalid": "Este nome de usuário não é válido.",
            },
            "password": {
                "invalid_login": "Nome de usuário ou senha incorretos.",
            },
        }


class CustomUserCreationForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Nome de usuário",
            "email": "E-mail",
            "password1": "Senha",
            "password2": "Confirme a senha",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={"placeholder": "Nome de usuário", "class": "form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "E-mail", "class": "form-control"}
            ),
            "password1": forms.PasswordInput(
                attrs={"placeholder": "Senha", "class": "form-control"}
            ),
            "password2": forms.PasswordInput(
                attrs={"placeholder": "Confirme a senha", "class": "form-control"}
            ),
        }
        help_texts = {
            "username": None,
            "password1": None,
            "password2": None,
        }
        error_messages = {
            "username": {
                "unique": "Este nome de usuário já está em uso.",
            },
            "email": {
                "unique": "Este e-mail já está em uso.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove os textos de ajuda diretamente nos campos de senha
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
