from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(tenant=user.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user.tenant)

    @action(detail=False, methods=["get"])
    def dashboard(self, request):
        qs = self.get_queryset()

        entradas = qs.filter(type="IN").aggregate(total=Sum("amount"))["total"] or 0
        saidas = qs.filter(type="OUT").aggregate(total=Sum("amount"))["total"] or 0

        return Response({
            "entradas": entradas,
            "saidas": saidas,
            "saldo": entradas - saidas
        })
