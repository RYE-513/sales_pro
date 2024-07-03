from django.db import models
from human_resources.models import Staff

class Branches(models.Model):
    id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=110)
    location = models.CharField(max_length=110)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateField(auto_now_add=True)



