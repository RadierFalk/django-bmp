from django.urls import path
from .views import (login_view, dashboard_view, create_transaction, delete_transaction,)

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('transactions/new/', create_transaction, name='create_transaction'),
    path('transactions/delete/<int:id>/', delete_transaction, name='delete_transaction'),
]
