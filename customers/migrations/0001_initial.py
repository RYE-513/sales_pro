# Generated by Django 5.0.2 on 2024-07-03 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
        ('human_resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=110)),
                ('status', models.CharField(choices=[('For Approval', 'PENDING'), ('Active', 'ACTIVE'), ('Disabled', 'DISABLED'), ('Deleted', 'DELETED')], default='PENDING', max_length=50)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('or_number', models.IntegerField()),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('For Approval', 'PENDING'), ('Active', 'ACTIVE'), ('Disabled', 'DISABLED'), ('Deleted', 'DELETED')], default='PENDING', max_length=50)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='branches.branches')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='human_resources.staff')),
            ],
        ),
    ]
