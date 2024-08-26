from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

import shop


def redirect_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return redirect("login")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_view, name="index"),
    path("home/", include("shop.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", shop.views.signup, name="signup"),
]
