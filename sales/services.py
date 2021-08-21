from validate_docbr import CPF

from resellers.models import Reseller


class SaleService:
    def __init__(self):
        self.cpf = CPF()
        self.allowed_cpf = [
            '15350946056'
        ]

    def validate_cpf_reseller(self, cpf: str) -> bool:
        return self.cpf.validate(cpf)

    @staticmethod
    def validate_cpf_exists(cpf: str) -> bool:
        return Reseller.objects.filter(cpf=cpf).exists()

    def get_status(self, cpf: str) -> str:
        return "APROVADO" if cpf in self.allowed_cpf else "EM_VALIDACAO"

    @staticmethod
    def get_status_from_instance(status: str) -> str:
        return status != "EM_VALIDACAO"
