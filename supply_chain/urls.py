from rest_framework.routers import DefaultRouter
from .views import  WarehouseViewSet, SupplyRequestViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet, basename='warehouses')
router.register(r'supplyreqs', SupplyRequestViewSet, basename='supplyreqs')
urlpatterns = router.urls

