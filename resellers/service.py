from validate_docbr import CPF


class ResellerService:
    def __init__(self):
        self.cpf = CPF()

    def validate_cpf(self, cpf) -> bool:
        return self.cpf.validate(cpf)

    def validate_password(self, password) -> bool:
        return len(password) >= 6
