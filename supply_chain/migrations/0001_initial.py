# Generated by Django 5.0.2 on 2024-04-18 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0003_rename_product_stocks_stock_product'),
        ('human_resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supply_Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('req_num', models.CharField(max_length=110)),
                ('date_requested', models.DateField()),
                ('driver_truck', models.CharField(max_length=110)),
                ('date_delivered', models.DateField()),
                ('status', models.CharField(choices=[('For Approval', 'PENDING'), ('Active', 'ACTIVE'), ('Disabled', 'DISABLED'), ('Deleted', 'DELETED')], default='PENDING', max_length=50)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('branch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.branches')),
                ('driver_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_supply_requests', to='human_resources.staff')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supply_requests', to='human_resources.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('warehouse_name', models.CharField(max_length=110)),
                ('location', models.CharField(max_length=110)),
                ('status', models.CharField(choices=[('For Approval', 'PENDING'), ('Active', 'ACTIVE'), ('Disabled', 'DISABLED'), ('Deleted', 'DELETED')], default='PENDING', max_length=50)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resources.staff')),
            ],
        ),
    ]
