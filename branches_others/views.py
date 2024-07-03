from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response  

from .serializers import SalesSerializer, StocksSerializer
from .models import Sales, Stocks

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = SalesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []

        for sales in queryset:
            sales_data = {
                'id': sales.id,
                'inv_no': sales.inv_no,
                'date': sales.date,
                'total_price': sales.total_price,
                'entry_by': sales.entry_by,
                'create_date': sales.create_date
            }
            data.append(sales_data)
        return Response(data)

class StocksViewSet(viewsets.ModelViewSet):
    queryset = Stocks.objects.all().order_by('id')
    serializer_class = StocksSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []

        for stocks in queryset:
            stocks_data = {
                'id': stocks.id,
                'category': stocks.category,
                'is_in': stocks.is_in,
                'create_date': stocks.create_date,
            }
            data.append(stocks_data)
        return Response(data)