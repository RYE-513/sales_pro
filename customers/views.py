from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response  

from .serializers import CustomerSerializer, TransactionsSerializer
from .models import Customer, Transactions

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []

        for customer in queryset:
            customer_data = {
                'id': customer.id,
                'customer_name': customer.customer_name,
                'status': customer.status,
                'create_date': customer.create_date
            }
            data.append(customer_data)
        return Response(data)
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = TransactionsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
    
        for transaction in queryset:
            branch_name = f"{transaction.branch.branch_name}" if transaction.branch else "No branch name assigned"
            staff_name = f"{transaction.staff.first_name} {transaction.staff.last_name}" if transaction.staff else "No staff assigned"
        
            transaction_data = {
                'id': transaction.id,
                'or_number': transaction.or_number,
                'branch' : branch_name,
                'staff' : staff_name,
                'payment_amount' : transaction.payment_amount,
                'change_amount' : transaction.change_amount,
                'grand_total' : transaction.grand_total,
                'date': transaction.date,
                'status': transaction.status,
                'create_date': transaction.create_date
            }
            data.append(transaction_data)
        return Response(data)
