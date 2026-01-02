from django.db import models
from tenants.models import Tenant

class Category(models.Model):
    name = models.CharField(max_length=100)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

class Transaction(models.Model):
    TYPE_CHOICES = (
        ('IN', 'Entrada'),
        ('OUT', 'Saída'),
    )

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    transaction_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    is_paid = models.BooleanField(default=False)
