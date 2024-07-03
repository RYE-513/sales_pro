from django.contrib import admin
from .models import Warehouse, Supply_Request

admin.site.register(Warehouse),
admin.site.register(Supply_Request)