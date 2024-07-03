from django.db import models
from branches.models import Branches
from human_resources.models import Staff
from products.models import Items

class Warehouse(models.Model):
    id=models.AutoField(primary_key=True)
    warehouse_name=models.CharField(max_length=110)
    location=models.CharField(max_length=110)
    staff=models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateField(auto_now_add=True)

class Supply_Request(models.Model):
    id=models.AutoField(primary_key=True)
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
    create_date = models.DateField(auto_now_add=True)

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=110)
    location = models.CharField(max_length=110)
    contact_number = models.CharField(max_length=110)
    contact_person = models.CharField(max_length=110)
    statusEnum = [("For Approval", "PENDING" ), ("Active", "ACTIVATE" ), ("Disabled", "DISABLE" ), ("Deleted", "DELETED" ),]
    status = models.CharField(max_length=50, choices=statusEnum, default="PENDING")
    create_date= models.DateTimeField(auto_now=True)

class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, db_column='supplier_id')
    po_number= models.IntegerField()
    delivery_address = models.CharField(max_length=110)
    delivery_date = models.DateField()
    total_order = models.FloatField()
    create_date= models.DateTimeField(auto_now=True)

class Item_Purchase_Order(models.Model):
    id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, db_column='purchase_id')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, db_column='item_id')
    qty = models.FloatField()
    create_date= models.DateTimeField(auto_now=True)
    
class Stock_Receivables(models.Model):
    id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, db_column='supplier_id')
    units = models.IntegerField()
    picked_up = models.IntegerField()
    create_date= models.DateTimeField(auto_now=True)
