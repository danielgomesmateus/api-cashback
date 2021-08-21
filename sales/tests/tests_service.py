from unittest import TestCase

from sales.services import SaleService, CashbackService


class SaleServiceTestCase(TestCase):
    pass


class CashbackServiceTestCase(TestCase):
    def test_get_value_cashback_if_is_valid_cpf(self):
        cpf = '99168306067'
        reseller_service = CashbackService()
        instance_service = reseller_service.get_value_cashback(cpf)
        self.assertTrue(instance_service)

    def test_get_value_cashback_if_is_not_valid_cpf(self):
        cpf = '99162201167'
        reseller_service = CashbackService()
        instance_service = reseller_service.get_value_cashback(cpf)
        self.assertFalse(instance_service)
