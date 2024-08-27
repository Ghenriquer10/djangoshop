from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.views import LoginView

# Importa formulário de criação de usuário
from .forms import CustomUserCreationForm, CustomLoginForm


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

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect("home")
