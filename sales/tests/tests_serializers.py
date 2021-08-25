from django.test import TestCase

from resellers.models import Reseller
from sales.api.serializers import SaleSerializer


class SaleSerializerTestCase(TestCase):
    def setUp(self):
        self.cpf_valid = '88073923050'
        self.cpf_invalid = '21451074000'

        reseller = Reseller(first_name='Daniel', last_name='Gomes Mateus', cpf='88073923050',
                            email='daniel.gomes@gmail.com')
        reseller.set_password('123456')
        reseller.save()
        
    def test_sale_serializer_if_data_is_valid(self):
        data = dict(code='d41d8cd98f00b204e9800998ecf8427e', amount='1250.87', date='2015-12-24',
                    cpf_reseller=self.cpf_valid, status='APROVADO')
        serializer = SaleSerializer(data=data)
        instance_serializer = serializer.is_valid()
        print(serializer.errors)
        self.assertTrue(instance_serializer)

    def test_sale_serializer_if_data_is_not_valid(self):
        data = dict(code='d41d8cd98f00b204e9800998ecf8427e', amount='1250.87', date='2015-12-24',
                    cpf_reseller=self.cpf_invalid, status='APROVADO')
        serializer = SaleSerializer(data=data)
        instance_serializer = serializer.is_valid()
        self.assertFalse(instance_serializer)
