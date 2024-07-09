from django.db import models
from supply_chain.models import Warehouse

class Sales(models.Model):
    inv_no = models.IntegerField()
    date = models.DateField()
    total_price = models.FloatField()
    entry_by = models.CharField(max_length=110)
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateField(auto_now_add=True)

class Stocks(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True)
    quantity= models.FloatField()
    create_date = models.DateField(auto_now_add=True)
