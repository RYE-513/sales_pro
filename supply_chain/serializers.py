from rest_framework import serializers
from .models import Warehouse, Supply_Request, Supplier, Purchase, Item_Purchase_Order, Stock_Receivables

class WarehousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class SupplyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply_Request
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.supplier_name', read_only=True)
    class Meta:
        model = Purchase
        fields = '__all__'

class Item_Purchase_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Purchase_Order
        fields = '__all__'

class Stock_ReceivablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_Receivables
        fields = '__all__'
