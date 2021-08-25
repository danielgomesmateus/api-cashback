from django.test import TestCase

from resellers.services import ResellerService


class ResellerServiceTestCase(TestCase):
    def test_validate_cpf_if_is_valid_cpf(self):
        cpf = '99168306067'
        reseller_service = ResellerService.validate_cpf(cpf)
        self.assertTrue(reseller_service)

    def test_validate_cpf_if_is_not_valid_cpf(self):
        cpf = '99162201167'
        reseller_service = ResellerService.validate_cpf(cpf)
        self.assertFalse(reseller_service)

    def test_validate_password_if_is_valid_password(self):
        cpf = '123456'
        reseller_service = ResellerService.validate_password(cpf)
        self.assertTrue(reseller_service)

    def test_validate_password_if_is_not_valid_password(self):
        cpf = '123'
        reseller_service = ResellerService.validate_password(cpf)
        self.assertFalse(reseller_service)
