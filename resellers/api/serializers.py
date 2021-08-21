from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from resellers.models import Reseller
from resellers.service import ResellerService


class ResellerSerializer(ModelSerializer):
    class Meta:
        model = Reseller
        fields = (
            'id',
            'first_name',
            'last_name',
            'cpf',
            'email',
            'password',
        )

    def validate_cpf(self, value):
        reseller_service = ResellerService()

        if not reseller_service.validate_cpf(value):
            raise serializers.ValidationError('Enter a valid CPF without periods and hyphen')
        return value

    def validate_password(self, value):
        reseller_service = ResellerService()

        if not reseller_service.validate_password(value):
            raise serializers.ValidationError('Enter a password with at least 6 digits')
        return value
