from django.db import models
from human_resources.models import Staff

class Trucks(models.Model):
    id = models.AutoField(primary_key=True)
    truck_name = models.CharField(max_length=255)
    truck_net_weight = models.IntegerField()
    plate_no = models.CharField(max_length=20)
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateField(auto_now_add=True)

class Drivers(models.Model):
    id = models.AutoField(primary_key=True)
    driver_name = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateField(auto_now_add=True)