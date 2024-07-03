from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Warehouse, Supply_Request, Supplier, Purchase, Item_Purchase_Order, Stock_Receivables 
from .serializers import WarehousesSerializer, SupplyRequestSerializer, SupplierSerializer,  PurchaseSerializer, Item_Purchase_OrderSerializer, Stock_ReceivablesSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = WarehousesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for warehouses in queryset:
            staff_name = f"{warehouses.staff.first_name} {warehouses.staff.last_name}"
            warehouses_data = {
                'id': warehouses.id,
                'warehouse_name': warehouses.warehouse_name,
                'location': warehouses.location,
                'caretaker': staff_name,
                'status': warehouses.status,
                'create_date': warehouses.create_date
            }
            data.append(warehouses_data)
        return Response(data)

class SupplyRequestViewSet(viewsets.ModelViewSet):
    queryset = Supply_Request.objects.all().order_by('id')
    serializer_class = SupplyRequestSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for supply_reqs in queryset:
            branch_name = f"{supply_reqs.branch_name.branch_name}"
            staff_name = f"{supply_reqs.staff.first_name} {supply_reqs.staff.last_name}"
            driver_staff = f"{supply_reqs.staff.first_name} {supply_reqs.staff.last_name}"
            
            supplyreqs_data = {
                'id': supply_reqs.id,
                'req_num' : supply_reqs.req_num,
                'staff' : staff_name,
                'branch' : branch_name,
                'date_requested' : supply_reqs.date_requested,
                'driver_staff' : driver_staff,
                'driver_truck' : supply_reqs.driver_truck,
                'date_delivered' : supply_reqs.date_delivered,
                'status': supply_reqs.status,
                'create_date': supply_reqs.create_date
            }
            data.append(supplyreqs_data)
        return Response(data)

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = SupplierSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('-id')
    serializer_class = PurchaseSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        item_purchase= Item_Purchase_Order.objects.filter(purchase=instance)
        item_purchase_serializer = Item_Purchase_OrderSerializer(item_purchase, many=True)
        response_data = {
            'purchase_data': serializer.data,
            'item_purchase_order': item_purchase_serializer.data
        }
        return Response(response_data)

class Item_Purchase_OrderViewSet(viewsets.ModelViewSet):
    queryset = Item_Purchase_Order.objects.all().order_by('id')
    serializer_class = Item_Purchase_OrderSerializer
    
class Stock_ReceivablesViewSet(viewsets.ModelViewSet):
    queryset = Stock_Receivables.objects.all().order_by('id')
    serializer_class = Stock_ReceivablesSerializer