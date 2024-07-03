from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'transaction', TransactionViewSet, basename='transaction')
urlpatterns = router.urls
