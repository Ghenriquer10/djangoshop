from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

urlpatterns = [
    path(
        "login/",
        CustomLoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("", views.home, name="home"),
]
