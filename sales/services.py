from validate_docbr import CPF

from resellers.models import Reseller


class SaleService:
    def __init__(self):
        self.cpf = CPF()
        self.allowed_cpf = [
            '15350946056'
        ]

    def validate_cpf_reseller(self, cpf) -> bool:
        return self.cpf.validate(cpf)

    def validate_cpf_exists(self, cpf) -> bool:
        return Reseller.objects.filter(cpf=cpf).exists()

    def get_status(self, cpf) -> str:
        return "APROVADO" if cpf in self.allowed_cpf else "EM_VALIDACAO"
