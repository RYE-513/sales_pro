from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import RolesSerializer, StaffSerializer
from .models import Roles, Staff

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = RolesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for roles in queryset:
            role_data = {
                'id': roles.id,
                'role': roles.role_name,
                'description': roles.description,
                'status': roles.status,
                'create_date': roles.create_date
            }
            data.append(role_data)
        return Response(data)

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = StaffSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for staff in queryset:
            role_name = f"{staff.role.role_name}"
            staff_data = {
                'id': staff.id,
                'first_name': staff.first_name,
                'last_name': staff.last_name,
                'role': role_name,
                'mobile_no' : staff.mobile_no,
                'email' : staff.email,
                'status': staff.status,
                'create_date': staff.create_date
            }
            data.append(staff_data)
        return Response(data)