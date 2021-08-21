from rest_framework.exceptions import APIException
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_400_BAD_REQUEST

from sales.models import Sale
from sales.api.serializers import SaleSerializer
from sales.services import SaleService


class SaleView(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    http_method_names = ['post', 'get', 'patch', 'delete']

    def perform_create(self, serializer: object) -> object:
        status = SaleService.get_status(serializer.initial_data.get('cpf_reseller'))

        instance = serializer.save(status=status)
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
