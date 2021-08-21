from rest_framework.viewsets import ModelViewSet

from sales.models import Sale
from sales.api.serializers import SaleSerializer
from sales.services import SaleService


class SaleView(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def perform_create(self, serializer):
        service_sale = SaleService()
        status = service_sale.get_status(serializer.initial_data.get('cpf_reseller'))

        instance = serializer.save(status=status)
        instance.save()
