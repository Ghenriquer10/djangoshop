from django.urls import include, path

from .views import home, index
from .views import CustomLoginView, adminView, home, signup

administrador_patterns = [
    path("", adminView, name="admin-index"),
]

cliente_patterns = [
    path("", home, name="home"),
]

vendedor_patterns = [
    path("", home, name="vendedor-index"),
]

estoquista_patterns = [
    path("", home, name="estoquista-index"),
]

urlpatterns = [
    path(
        "login/",
        CustomLoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("signup/", signup, name="signup"),
    path("", index, name="index"),
    path("cliente/", include(cliente_patterns)),
    path("vendedor/", include(vendedor_patterns)),
    path("estoquista/", include(estoquista_patterns)),
    path("administrador/", include(administrador_patterns)),
]
