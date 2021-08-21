from sales.services import SaleService


class SaleRepository:
    def __init__(self):
        self.sale_service = SaleService()

    @staticmethod
    def create(serializer: object, data):
        instance = serializer.save(status=data.get('status'), cashback=data.get('cashback'),
                                   per_cent_cashback=data.get('per_cent_cashback'))
        instance.save()

    @staticmethod
    def update(serializer: object, data):
        instance = serializer.save(status=data.get('status'), cashback=data.get('cashback'),
                                   per_cent_cashback=data.get('per_cent_cashback'))
        instance.save()

    @staticmethod
    def destroy(instance: object):
        instance.delete()
