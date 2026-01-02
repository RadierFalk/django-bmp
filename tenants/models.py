from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
