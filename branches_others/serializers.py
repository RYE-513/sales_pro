from rest_framework import serializers
from .models import Sales, Stocks
# from supply_chain.serializers import WarehousesSerializer

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class StocksSerializer(serializers.ModelSerializer):
    # stock_warehouse = WarehousesSerializer()
    class Meta:
        model = Stocks
        fields = '__all__'