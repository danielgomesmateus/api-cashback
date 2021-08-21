from validate_docbr import CPF


class ResellerService:
    @staticmethod
    def validate_cpf(cpf: str) -> bool:
        cpf_instance = CPF()
        return cpf_instance.validate(cpf)

    @staticmethod
    def validate_password(password: str) -> bool:
        return len(password) >= 6
