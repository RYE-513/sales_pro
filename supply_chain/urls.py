from rest_framework.routers import DefaultRouter
from .views import  WarehouseViewSet, SupplyRequestViewSet, SupplierViewSet, PurchaseViewSet, Item_Purchase_OrderViewSet, Stock_ReceivablesViewSet

router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet, basename='warehouses')
router.register(r'supplyreqs', SupplyRequestViewSet, basename='supplyreqs')
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'purchase', PurchaseViewSet, basename='purchase')
router.register(r'item_purchase', Item_Purchase_OrderViewSet, basename='item_purchase')
router.register(r'stock_receivables', Stock_ReceivablesViewSet, basename='stock_receivables')
urlpatterns = router.urls