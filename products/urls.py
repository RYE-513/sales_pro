from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet, PackagesViewSet, ItemsViewSet, ProductsViewSet
router = DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'packages', PackagesViewSet, basename='packages')
router.register(r'items', ItemsViewSet, basename='items')
urlpatterns = router.urls
