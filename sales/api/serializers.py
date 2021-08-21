from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from sales.models import Sale
from sales.services import SaleService


class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = (
            'id',
            'code',
            'amount',
            'date',
            'cpf_reseller',
        )

    def validate_cpf_reseller(self, value):
        sale_service = SaleService()

        if not sale_service.validate_cpf_reseller(value):
            raise serializers.ValidationError('Enter a valid CPF without periods and hyphen')
        if not sale_service.validate_cpf_exists(value):
            raise serializers.ValidationError('There is no reseller associated with this CPF')
        return value
