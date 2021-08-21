from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from sales.models import Sale
from sales.services import SaleService


class SaleSerializer(ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            'id',
            'code',
            'amount',
            'date',
            'cpf_reseller',
            'status',
        )

    @staticmethod
    def validate_cpf_reseller(value: str) -> str:
        sale_service = SaleService()

        if not sale_service.validate_cpf_reseller(value):
            raise serializers.ValidationError('Enter a valid CPF without periods and hyphen')
        if not SaleService.validate_cpf_exists(value):
            raise serializers.ValidationError('There is no reseller associated with this CPF')
        return value

    def get_status(self, value: str) -> str:
        sale_service = SaleService()
        return sale_service.get_status(self.initial_data.get('cpf_reseller'))
