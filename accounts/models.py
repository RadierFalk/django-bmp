from django.contrib.auth.models import AbstractUser
from django.db import models
from tenants.models import Tenant

class User(AbstractUser):
    ROLE_CHOICES = (
        ('DEV', 'Desenvolvedor'),
        ('ADMIN', 'Administrador Contábil'),
        ('ACCOUNTANT', 'Contador'),
        ('CLIENT', 'Cliente'),
    )
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )  

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
