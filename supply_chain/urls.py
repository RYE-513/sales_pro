from django.urls import path
from . import views

app_name = 'supply_chain'

urlpatterns = [

    # WAREHOUSE

    path('warehouse/', views.warehouseList, name='warehouse'),
    path('add_warehouse/', views.add_warehouse, name='add_warehouse'),
    path('deleted_warehouseList/', views.deleted_warehouseList, name='deleted_warehouseList'),

    path('update_warehouse/<int:pk>/', views.update_warehouse, name='update_warehouse'),
    path('update_warehouse_status/<int:pk>/', views.update_warehouse_status, name='update_warehouse_status'),
    path('delete_warehouse/<int:pk>/', views.delete_warehouse, name='delete_warehouse'),
    path('recover_warehouse/<int:pk>/', views.recover_warehouse, name='recover_warehouse'),

    # SUPPLY CHAIN

    path('supply_reqs/', views.supplyreqsList, name='supply_reqs'),
    path('add_supplyreqs/', views.add_supplyreqs, name='add_supplyreqs'),
    path('deleted_supplyreqsList/', views.deleted_supplyreqsList, name='deleted_supplyreqsList'),

    path('update_supplyreqs/<int:pk>/', views.update_supplyreqs, name='update_supplyreqs'),
    path('update_supplyreqs_status/<int:pk>/', views.update_supplyreqs_status, name='update_supplyreqs_status'),
    path('delete_supplyreqs/<int:pk>/', views.delete_supplyreqs, name='delete_supplyreqs'),
    path('recover_supplyreqs/<int:pk>/', views.recover_supplyreqs, name='recover_supplyreqs'),

]