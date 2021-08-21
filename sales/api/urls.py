from rest_framework.routers import SimpleRouter

from sales.views import SaleView

app_name = 'sales'

router = SimpleRouter()
router.register('sales', SaleView)
