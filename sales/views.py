from rest_framework.exceptions import APIException
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_400_BAD_REQUEST

from sales.models import Sale
from sales.api.serializers import SaleSerializer, SaleListSerializer
from sales.services import SaleService


class SaleView(ModelViewSet):
    queryset = Sale.objects.all()
    default_serializer_class = SaleSerializer
    http_method_names = ['post', 'get', 'patch', 'delete']
    serializer_classes = {
        'list': SaleListSerializer,
        'retrieve': SaleListSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def perform_create(self, serializer: object) -> object:
        cpf = serializer.initial_data.get('cpf_reseller')
        amount = serializer.initial_data.get('amount')

        sale_service = SaleService()
        status = sale_service.get_status(cpf)
        cashback, per_cent_cashback = sale_service.get_value_cashback(amount)

        instance = serializer.save(status=status, cashback=cashback, per_cent_cashback=per_cent_cashback)
        instance.save()

    def perform_update(self, serializer: object) -> object:
        if SaleService.get_status_from_instance(serializer.instance.status):
            raise APIException("The data for this sale cannot be changed", code=HTTP_400_BAD_REQUEST)
        instance = serializer.save()
        instance.save()

    def perform_destroy(self, instance: object) -> object:
        if SaleService.get_status_from_instance(instance.status):
            raise APIException("The data for this sale cannot be deleted", code=HTTP_400_BAD_REQUEST)
        instance.delete()
