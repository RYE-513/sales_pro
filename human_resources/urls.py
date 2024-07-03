from rest_framework.routers import DefaultRouter
from .views import RolesViewSet, StaffViewSet
router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'roles', RolesViewSet, basename='roles')
urlpatterns = router.urls