from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response  

from .serializers import TrucksSerializer, DriversSerializer
from .models import Trucks, Drivers

class TrucksViewSet(viewsets.ModelViewSet):
    queryset = Trucks.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = TrucksSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []

        for truck in queryset:
            truck_data = {
                'id': truck.id,
                'truck_name': truck.truck_name,
                'truck_net_weight': truck.truck_net_weight,
                'plate_no': truck.plate_no,
                'status': truck.status,
                'create_date': truck.create_date
            }
            data.append(truck_data)
        return Response(data)
    
class DriversViewSet(viewsets.ModelViewSet):
    queryset = Drivers.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = DriversSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []

        for driver in queryset:
            staff_name = f"{driver.driver_name.first_name} {driver.driver_name.last_name}" if driver.driver_name else "No staff assigned"
            driver_data = {
                'id': driver.id,
                'staff': staff_name,
                'status': driver.status,
                'create_date': driver.create_date
            }
            data.append(driver_data)
        return Response(data)

