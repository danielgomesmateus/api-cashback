from django.test import TestCase

from sales.services import SaleService
from sales.models import Sale
from resellers.models import Reseller


class SaleServiceTestCase(TestCase):
    def setUp(self):
        reseller = Reseller(first_name='Daniel', last_name='Gomes Mateus', cpf='88073923050',
                            email='daniel.gomes@gmail.com')
        reseller.set_password('123456')
        reseller.save()
        Sale.objects.create(code='d41d8cd98f00b204e9800998ecf8427e', amount='320.98', cashback='32.10',
                            per_cent_cashback='10', date='2020-10-22', cpf_reseller='88073923050',
                            status='EM_VALIDACAO')

    def test_validate_cpf_reseller_if_cpf_is_valid(self):
        cpf = '88073923050'
        instance_service = SaleService.validate_cpf_reseller(cpf)
        self.assertTrue(instance_service)

    def test_validate_cpf_reseller_if_cpf_is_not_valid(self):
        cpf = '88071923050'
        instance_service = SaleService.validate_cpf_reseller(cpf)
        self.assertFalse(instance_service)

    def test_validate_cpf_exists_if_cpf_exists(self):
        cpf = '88073923050'
        instance_service = SaleService.validate_cpf_exists(cpf)
        self.assertTrue(instance_service)

    def test_validate_cpf_exists_if_cpf_not_exists(self):
        cpf = '88071923050'
        instance_service = SaleService.validate_cpf_exists(cpf)
        self.assertFalse(instance_service)

    def test_get_status_if_cpf_is_allowed(self):
        cpf = '15350946056'
        sale_service = SaleService()
        instance_service = sale_service.get_status(cpf)
        self.assertEqual(instance_service, 'APROVADO')

    def test_get_status_if_cpf_is_not_allowed(self):
        cpf = '88073923050'
        sale_service = SaleService()
        instance_service = sale_service.get_status(cpf)
        self.assertEqual(instance_service, 'EM_VALIDACAO')

    def test_get_status_from_instance_if_status_is_valid(self):
        status = 'APROVADO'
        instance_service = SaleService.get_status_from_instance(status)
        self.assertTrue(instance_service)

    def test_get_status_from_instance_if_status_is_not_valid(self):
        status = 'EM_VALIDACAO'
        instance_service = SaleService.get_status_from_instance(status)
        self.assertFalse(instance_service)

    def test_get_value_cashback_until_1000(self):
        amount = 1000
        sale_service = SaleService()
        cashback, per_cent = sale_service.get_value_cashback(amount)
        self.assertEqual(cashback, 100)
        self.assertEqual(per_cent, 10)

    def test_get_value_cashback_until_1500(self):
        amount = 1500
        sale_service = SaleService()
        cashback, per_cent = sale_service.get_value_cashback(amount)
        self.assertEqual(cashback, 225)
        self.assertEqual(per_cent, 15)

    def test_get_value_cashback_above_1500(self):
        amount = 1600
        sale_service = SaleService()
        cashback, per_cent = sale_service.get_value_cashback(amount)
        self.assertEqual(cashback, 320)
        self.assertEqual(per_cent, 20)

