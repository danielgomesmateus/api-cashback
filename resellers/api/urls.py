from rest_framework.routers import SimpleRouter

from resellers.views import ResellerView

app_name = 'resellers'

router = SimpleRouter()
router.register('resellers', ResellerView)
