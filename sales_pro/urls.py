from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('session.urls', namespace='session')),
    path('analytics/',include('analytics.urls', namespace='analytics')),
    path('',include('branches.urls', namespace='branches')),

    path('',include('human_resources.urls', namespace='human_resources')),
    path('',include('supply_chain.urls', namespace='supply_chain')),

]