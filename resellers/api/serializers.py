from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from resellers.models import Reseller
from resellers.services import ResellerService


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

    @staticmethod
    def validate_cpf(value: str) -> str:
        if not ResellerService.validate_cpf(value):
            raise serializers.ValidationError('Enter a valid CPF without periods and hyphen')
        return value

    @staticmethod
    def validate_password(value: str) -> str:
        if not ResellerService.validate_password(value):
            raise serializers.ValidationError('Enter a password with at least 6 digits')
        return value
