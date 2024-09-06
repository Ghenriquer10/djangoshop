from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Importa formulário de criação de usuário
from .forms import CustomUserCreationForm, CustomLoginForm

# shop/views.py
from shop.models import PapeisDeUsuario


def index(request):
    user = request.user
    if user.is_authenticated:
        papel = user.get_papel()
        print(papel)
        if papel == PapeisDeUsuario.ADMINISTRADOR:
            return redirect(reverse("admin-index"))
        elif papel == PapeisDeUsuario.CLIENTE:
            return redirect(reverse("home"))
        elif papel == PapeisDeUsuario.VENDEDOR:
            return redirect(reverse("vendedor-index"))
        elif papel == PapeisDeUsuario.ESTOQUISTA:
            return redirect(reverse("estoquista-index"))
    else:
        return redirect(reverse("login"))


@login_required
def home(request):
    # Sua lógica aqui
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "registration/login.html"


def adminView(request):
    return render(request, "administrador/admin_index.html")
