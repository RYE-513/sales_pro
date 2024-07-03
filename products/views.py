from rest_framework import viewsets
from .models import Categories, Packages, Items, Cost, Price, Products
from .serializers import ProductsSerializer, CategoriesSerializer, PackagesSerializer, ItemsSerializer, CostSerializer, PriceSerializer 
from rest_framework.response import Response

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('-id')
    serializer_class = ProductsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        items= Items.objects.filter(products=instance)
        items_serializer = ItemsSerializer(items, many=True)
        response_data = {
            'products_data': serializer.data,
            'items': items_serializer.data
        }
        return Response(response_data)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('-id')
    serializer_class = CategoriesSerializer

class PackagesViewSet(viewsets.ModelViewSet):
    queryset = Packages.objects.all().order_by('-id')
    serializer_class = PackagesSerializer
    
class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.filter(status__in=['Active']).order_by('-id')
    serializer_class = ItemsSerializer

class CostViewSet(viewsets.ModelViewSet):
    queryset = Cost.objects.all().order_by('id')
    serializer_class = CostSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all().order_by('id')
    serializer_class = PriceSerializer