from rest_framework.exceptions import APIException
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated

from sales.models import Sale
from sales.api.serializers import SaleSerializer, SaleListSerializer
from sales.services import SaleService, CashbackService
from sales.repositories import SaleRepository


class SaleView(ModelViewSet):
    queryset = Sale.objects.all()
    default_serializer_class = SaleSerializer
    http_method_names = ['post', 'get', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    serializer_classes = {
        'list': SaleListSerializer,
        'retrieve': SaleListSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def perform_create(self, serializer: object):
        data = self.get_data(serializer.initial_data.get('cpf_reseller'), serializer.initial_data.get('amount'))
        SaleRepository.create(serializer, data)

    def perform_update(self, serializer: object):
        if SaleService.get_status_from_instance(serializer.instance.status):
            raise APIException("The data for this sale cannot be changed")
        data = self.get_data(serializer.instance.cpf_reseller, serializer.instance.amount)
        SaleRepository.create(serializer, data)

    def perform_destroy(self, instance: object):
        if SaleService.get_status_from_instance(instance.status):
            raise APIException("The data for this sale cannot be deleted")
        SaleRepository.destroy(instance)

    @staticmethod
    def get_data(cpf: str, amount: str) -> dict:
        sale_service = SaleService()
        status = sale_service.get_status(cpf)
        cashback, per_cent_cashback = sale_service.get_value_cashback(amount)

        return dict(status=status, cashback=cashback, per_cent_cashback=per_cent_cashback)


class CashbackView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, cpf: str) -> object:
        if SaleService.validate_cpf_exists(cpf):
            cashback_service = CashbackService()
            cashback = cashback_service.get_value_cashback(cpf)
            return Response(data=cashback, status=HTTP_200_OK)
        return Response(data={"message": "CPF not found"}, status=HTTP_400_BAD_REQUEST)
