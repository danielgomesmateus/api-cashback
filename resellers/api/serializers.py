from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from resellers.models import Reseller


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
