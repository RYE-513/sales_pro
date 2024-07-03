from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('session.urls', namespace='session')),
    path('api/', include('branches.urls')),
    path('api/', include('branches_others.urls')),
    path('api/', include('human_resources.urls')),
    path('api/', include('supply_chain.urls')),
    path('api/', include('products.urls')),


    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)