import requests
from rest_framework.exceptions import APIException
from validate_docbr import CPF

from resellers.models import Reseller


class SaleService:
    def __init__(self):
        self.allowed_cpf = [
            '15350946056'
        ]

    @staticmethod
    def validate_cpf_reseller(cpf: str) -> bool:
        cpf_instance = CPF()
        return cpf_instance.validate(cpf)

    @staticmethod
    def validate_cpf_exists(cpf: str) -> bool:
        return Reseller.objects.filter(cpf=cpf).exists()

    def get_status(self, cpf: str) -> str:
        return "APROVADO" if cpf in self.allowed_cpf else "EM_VALIDACAO"

    @staticmethod
    def get_status_from_instance(status: str) -> str:
        return status != "EM_VALIDACAO"

    def get_value_cashback(self, amount: str) -> float:
        per_cent = self.get_per_cent_cashback(amount)
        amount = float(amount)
        
        return (amount * per_cent) / 100, per_cent

    @staticmethod
    def get_per_cent_cashback(amount: str) -> int:
        amount = float(amount)

        if amount <= 1000:
            return 10
        elif 1001 <= amount <= 1500:
            return 15
        else:
            return 20


class CashbackService:
    def __init__(self):
        self.base_url = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/'

    def get_value_cashback(self, cpf: str) -> object:
        url = '{}cashback?cpf={}'.format(self.base_url, cpf)
        r = requests.get(url)

        if r.status_code == 200:
            return r.json().get('body')
        raise APIException("Error fetching cashback information")
