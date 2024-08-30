from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

import shop
import shop.urls

urlpatterns = [
    path("", include(shop.urls)),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", shop.views.signup, name="signup"),
]
