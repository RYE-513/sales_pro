# Generated by Django 5.0.2 on 2024-04-18 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('supply_chain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('po_number', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=110)),
                ('delivery_date', models.DateField()),
                ('total_order', models.FloatField()),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=110)),
                ('location', models.CharField(max_length=110)),
                ('contact_number', models.CharField(max_length=110)),
                ('contact_person', models.CharField(max_length=110)),
                ('status', models.CharField(choices=[('For Approval', 'PENDING'), ('Active', 'ACTIVATE'), ('Disabled', 'DISABLE'), ('Deleted', 'DELETED')], default='PENDING', max_length=50)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Purchase_Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.FloatField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(db_column='item_id', on_delete=django.db.models.deletion.CASCADE, to='products.items')),
                ('purchase', models.ForeignKey(db_column='purchase_id', on_delete=django.db.models.deletion.CASCADE, to='supply_chain.purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Receivables',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('units', models.IntegerField()),
                ('picked_up', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('supplier', models.ForeignKey(db_column='supplier_id', on_delete=django.db.models.deletion.CASCADE, to='supply_chain.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='supplier',
            field=models.ForeignKey(db_column='supplier_id', on_delete=django.db.models.deletion.CASCADE, to='supply_chain.supplier'),
        ),
    ]
