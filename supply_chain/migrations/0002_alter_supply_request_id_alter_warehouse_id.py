# Generated by Django 5.0.2 on 2024-07-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply_chain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply_request',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
