from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response  

from .serializers import BranchesSerializer
from .models import Branches

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.filter(status__in=['Active']).order_by('id')
    serializer_class = BranchesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = []
        for branch in queryset:
            staff_name = f"{branch.staff.first_name} {branch.staff.last_name}"
            branch_data = {
                'id': branch.id,
                'branch_name': branch.branch_name,
                'location': branch.location,
                'manager': staff_name,
                'status': branch.status,
                'create_date': branch.create_date
            }
            data.append(branch_data)
        return Response(data)