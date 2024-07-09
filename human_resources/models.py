from django.db import models

class Roles(models.Model):
    role_name = models.CharField(max_length=110)
    description = models.TextField()
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateField(auto_now_add=True)

class Staff(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column="role_id")  # Set a default role ID
    first_name = models.CharField(max_length=110) 
    last_name = models.CharField(max_length=110)
    mobile_no = models.CharField(max_length=50)
    email = models.CharField(max_length=110)
    STATUS_CHOICES = [
        ("For Approval", "PENDING"),
        ("Active", "ACTIVE"),
        ("Disabled", "DISABLED"),
        ("Deleted", "DELETED"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="PENDING")
    create_date = models.DateField(auto_now_add=True)