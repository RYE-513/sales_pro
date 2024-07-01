from django.urls import path
from . import views
from session.views import LoginView, RegistrationView, TenantLoginView, DashboardView, SignoutView, UserProfileView

app_name = 'session'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    path('signout/', SignoutView.as_view(), name='signout'),
    path('protected/', views.protected_view, name='protected_view'),
]

