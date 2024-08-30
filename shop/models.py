from django.db import models

# Implementa model de usuário customizado com email, telefone e endereço

from django.contrib.auth.models import AbstractUser


class PapeisDeUsuario:
    ADMINISTRADOR = "ADMINISTRADOR"
    CLIENTE = "CLIENTE"
    VENDEDOR = "VENDEDOR"
    ESTOQUISTA = "ESTOQUISTA"


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_administrator = models.BooleanField(default=False)

    papel = models.CharField(
        max_length=20,
        choices=[
            (PapeisDeUsuario.ADMINISTRADOR, "Administrador"),
            (PapeisDeUsuario.CLIENTE, "Cliente"),
            (PapeisDeUsuario.VENDEDOR, "Vendedor"),
            (PapeisDeUsuario.ESTOQUISTA, "Estoquista"),
        ],
        default=PapeisDeUsuario.CLIENTE,
    )

    def get_papel(self):
        if self.is_administrator:
            return PapeisDeUsuario.ADMINISTRADOR
        elif self.papel == PapeisDeUsuario.CLIENTE:
            return PapeisDeUsuario.CLIENTE
        elif self.papel == PapeisDeUsuario.VENDEDOR:
            return PapeisDeUsuario.VENDEDOR
        elif self.papel == PapeisDeUsuario.ESTOQUISTA:
            return PapeisDeUsuario.ESTOQUISTA

    def __str__(self):
        return self.email
