from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from resellers.models import Reseller
from sales.views import SaleView, CashbackView
from sales.models import Sale


class SaleViewTestCase(TestCase):
    def setUp(self) -> None:
        self.cpf_valid = '93367323071'
        self.cpf_invalid = '93367783071'

        reseller = Reseller(first_name='Luiza', last_name='Almeida', cpf='93367323071',
                            email='luiza.almeida@gmail.com')
        reseller.set_password('123456')
        reseller.save()
        Sale.objects.create(code='d41d8cd98f00b204e2000998ecf8427e', amount='320.98', cashback='32.10',
                            per_cent_cashback='10', date='2020-10-22', cpf_reseller='93367323071',
                            status='APROVADO')
        Sale.objects.create(code='d41d8cd98f00b204e9800998ecf8427e', amount='320.98', cashback='32.10',
                            per_cent_cashback='10', date='2020-10-22', cpf_reseller='93367323071',
                            status='EM_VALIDACAO')

        data = dict(email='luiza.almeida@gmail.com', password='123456')

        self.client = Client()
        response = self.client.post(reverse('token_obtain_pair'), data=data)
        self.token = response.json().get('access')
        self.bearer = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.token)}

    def test_perform_delete_if_status_approve(self):
        pass
        # sale = Sale.objects.get(code='d41d8cd98f00b204e2000998ecf8427e')
        #
        # request = RequestFactory().delete(reverse('sales-detail', kwargs={'pk': sale.id}), **self.bearer)
        # response = SaleView.as_view({'delete': 'destroy'})(request)
        # self.assertEqual(response.status_code, 200)


class CashbackViewTestCase(TestCase):
    def setUp(self) -> None:
        self.base_url = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/'
        self.cpf_valid = '88073923050'
        self.cpf_invalid = '25963589659'

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

    def test_get_if_cpf_is_invalid(self):
        request = RequestFactory().get(reverse('cashback', kwargs={'cpf': self.cpf_invalid}), **self.bearer)
        response = CashbackView.as_view()(request, self.cpf_invalid)
        self.assertEqual(response.status_code, 400)
