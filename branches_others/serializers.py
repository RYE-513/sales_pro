from rest_framework import serializers
from .models import Sales, In_Out, Stocks

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class InOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = In_Out
        fields = '__all__'

class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = '__all__'