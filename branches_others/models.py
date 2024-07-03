from django.db import models
from human_resources.models import Staff
from products.models import Products, Categories
from supply_chain.models import Warehouse

class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    inv_no = models.IntegerField()
    date = models.DateField()
    total_price = models.FloatField()
    entry_by = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateField(auto_now_add=True)

class In_Out(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_in = models.BooleanField()
    create_date= models.DateField(auto_now=True)

class Stocks(models.Model):
    id = models.AutoField(primary_key=True)
    stock_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    stock_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    stock_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    in_out = models.ForeignKey(In_Out, on_delete=models.CASCADE)
    quantity= models.FloatField()
    create_date= models.DateTimeField(auto_now=True)