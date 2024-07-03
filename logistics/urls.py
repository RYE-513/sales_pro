from rest_framework.routers import DefaultRouter
from .views import TrucksViewSet, DriversViewSet

router = DefaultRouter()
router.register(r'truck', TrucksViewSet, basename='truck')
router.register(r'driver', DriversViewSet, basename='driver')
urlpatterns = router.urls
