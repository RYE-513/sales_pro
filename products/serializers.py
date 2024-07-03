from rest_framework import serializers
from .models import Products, Categories, Packages, Items, Cost, Price

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True, read_only=True)  
    category_name = serializers.CharField(source='category.category_name', read_only=True)
    package_name = serializers.CharField(source='package.package_name', read_only=True)

    class Meta:
        model = Products
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packages
        fields = '__all__'

class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'