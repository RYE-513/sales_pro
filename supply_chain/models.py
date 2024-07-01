from django.db import models
from django.views import View

from branches.models import Branches
from human_resources.models import Staff

class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=110)
    location = models.CharField(max_length=110)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = [
        ("Active", "ACTIVE"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateTimeField(auto_now=True)
class Supply_Request(models.Model):
    req_num = models.CharField(max_length=110)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='supply_requests')  # Renamed related_name
    branch_name = models.ForeignKey(Branches, on_delete=models.CASCADE)
    date_requested = models.DateField()
    driver_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='driver_supply_requests')  # Renamed and fixed field name
    driver_truck = models.CharField(max_length=110)
    date_delivered = models.DateField()
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateTimeField(auto_now=True)

