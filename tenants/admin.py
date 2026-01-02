from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'is_active', 'created_at')
    search_fields = ('name', 'cnpj')
    list_filter = ('is_active',)
