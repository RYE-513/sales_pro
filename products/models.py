from django.db import models
from django.http import JsonResponse

class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=110)
    statusEnum = [("For Approval", "PENDING" ), ("Active", "ACTIVATE" ), ("Disabled", "DISABLE" ), ("Deleted", "DELETED" ),]
    status = models.CharField(max_length=50, choices=statusEnum, default="PENDING")
    create_date= models.DateTimeField(auto_now=True)

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=110)
    description = models.TextField()
    statusEnum = [("For Approval", "PENDING" ), ("Active", "ACTIVATE" ), ("Disabled", "DISABLE" ), ("Deleted", "DELETED" ),]
    status = models.CharField(max_length=50, choices=statusEnum, default="PENDING")
    create_date= models.DateTimeField(auto_now=True)

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=100, null=True)
    product_name = models.CharField(max_length=110)
    product_package = models.ForeignKey(Packages, on_delete=models.CASCADE, db_column='package_id')
    product_category = models.ForeignKey(Categories, on_delete=models.CASCADE, db_column = 'category_id')
    current_price= models.FloatField()
    current_cost= models.FloatField()
    statusEnum = [("For Approval", "PENDING" ), ("Active", "ACTIVATE" ), ("Disabled", "DISABLE" ), ("Deleted", "DELETED" ),]
    status = models.CharField(max_length=50, choices=statusEnum, default="PENDING")
    create_date = models.DateTimeField( auto_now=True)

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=110)
    # items_package = models.ForeignKey(Packages, on_delete=models.CASCADE, db_column='package_id')
    # items_category = models.ForeignKey(Categories, on_delete=models.CASCADE, db_column='category_id')
    statusEnum = [("For Approval", "PENDING" ), ("Active", "ACTIVATE" ), ("Disabled", "DISABLE" ), ("Deleted", "DELETED" ),]
    status = models.CharField(max_length=50, choices=statusEnum, default="PENDING")
    create_date = models.DateTimeField( auto_now=True)  

class Price(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null= True)
    price = models.FloatField()
    create_date= models.DateTimeField(auto_now=True)

class Cost(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null= True)
    cost = models.FloatField()
    create_date= models.DateTimeField(auto_now=True)