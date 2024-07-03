from rest_framework import serializers
from .models import Warehouse, Supply_Request

class WarehousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class SupplyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply_Request
        fields = '__all__'
