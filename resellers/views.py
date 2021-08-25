from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from resellers.models import Reseller
from resellers.api.serializers import ResellerSerializer


class ResellerView(ModelViewSet):
    queryset = Reseller.objects.all()
    serializer_class = ResellerSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
