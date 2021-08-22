from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from resellers.models import Reseller
from sales.views import SaleView, CashbackView


class CashbackViewTestCase(TestCase):
    def setUp(self) -> None:
        self.base_url = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/'
        self.cpf_valid = '88073923050'
        self.cpf_invalid = ''

        reseller = Reseller(first_name='Daniel', last_name='Gomes Mateus', cpf='88073923050',
                            email='daniel.gomes@gmail.com')
        reseller.set_password('123456')
        reseller.save()

        data = dict(email='daniel.gomes@gmail.com', password='123456')

        self.client = Client()
        response = self.client.post(reverse('token_obtain_pair'), data=data)
        self.token = response.json().get('access')
        self.bearer = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.token)}

    def test_get_if_user_is_not_authenticated(self):
        request = RequestFactory().get(reverse('cashback', args={'cpf': self.cpf_valid}))
        response = CashbackView.as_view()(request, self.cpf_valid)
        self.assertEqual(response.status_code, 401)

    def test_get_if_user_is_authenticated(self):
        request = RequestFactory().get(reverse('cashback', kwargs={'cpf': self.cpf_valid}), **self.bearer)
        response = CashbackView.as_view()(request, self.cpf_valid)
        self.assertEqual(response.status_code, 200)
