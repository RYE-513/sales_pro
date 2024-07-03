from rest_framework.routers import DefaultRouter
from .views import SalesViewSet, StocksViewSet

router = DefaultRouter()
router.register(r'sales', SalesViewSet, basename='sales')
router.register(r'stocks', StocksViewSet, basename='stocks')

urlpatterns = router.urls
