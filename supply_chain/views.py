from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from django.http import HttpResponse

from branches.models import Branches
from human_resources.models import Staff
from .models import Warehouse, Supply_Request

##########  ##########  WAREHOUSING  ##########  ##########

# WAREHOUSE TABLE

def warehouseList(request):
    warehouse = Warehouse.objects.all().order_by('id')
    staff = Staff.objects.all().order_by('id').filter(status='ACTIVE')

    context ={
        'warehouse_list': warehouse,
        'staff_list': staff,
    }

    return render(request, 'supply_chain/warehouse-list.html', context)

# ADD DATA WAREHOUSE TABLE

def add_warehouse(request):
    if request.method == 'POST':
        warehouse_name = request.POST.get('warehouse_name')
        location = request.POST.get('location')
        staff_id = request.POST.get('staff_id')

        warehouse_get = Warehouse (
            warehouse_name=warehouse_name,
            location=location,
            staff_id=staff_id,
        )

        warehouse_get.save()
        return redirect('supply_chain:warehouse')
    
# DELETE DATA WAREHOUSE TABLE

def deleted_warehouseList(request):
    warehouse = Warehouse.objects.filter(status__in=['DELETED'])
    context = {
        'warehouse_list': warehouse,
    }

    return render(request, 'supply_chain/warehouse-deleted.html', context)

# WAREHOUSE ACTIONS MODALS

def update_warehouse(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        warehouse.warehouse_name = request.POST.get('warehouse_name_edit')
        warehouse.location = request.POST.get('location_edit')
        warehouse.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def update_warehouse_status(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        warehouse.status = request.POST.get('status_status')
        warehouse.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_warehouse(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        warehouse.status = "DELETED"
        warehouse.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def recover_warehouse(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        warehouse.status = "ACTIVE"
        warehouse.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

##########  ##########  SUPPLY REQUEST  ##########  ##########

# SUPPLY REQUEST TABLE

def supplyreqsList(request):
    supply_reqs = Supply_Request.objects.all().order_by('id')
    staff = Staff.objects.all().order_by('id')
    branch = Branches.objects.all().order_by('id')

    context = {
        'supplyreqs_list' : supply_reqs,
        'staff_list': staff,
        'branch_list': branch,
    }

    return render(request, 'supply_chain/supply_request-list.html', context)

# ADD DATA SUPPLY REQUEST TABLE

def add_supplyreqs(request):
    if request.method == 'POST':
        req_num = request.POST.get('req_num')
        staff_id = request.POST.get('staff_id')
        branch_id = request.POST.get('branch_id')
        date_requested = request.POST.get('date_requested')
        driver_staff_id = request.POST.get('driver_staff')
        driver_truck = request.POST.get('driver_truck')
        date_delivered = request.POST.get('date_delivered')

        supply_reqs_get = Supply_Request (
            req_num=req_num,
            staff_id=staff_id,
            branch_name_id=branch_id,
            date_requested=date_requested,
            driver_staff_id=driver_staff_id,
            driver_truck=driver_truck,
            date_delivered=date_delivered,
        )

        supply_reqs_get.save()
        return redirect('supply_chain:supply_reqs')

# DELETE DATA SUPPLY REQUEST TABLE

def deleted_supplyreqsList(request):
    supply_reqs = Supply_Request.objects.filter(status__in=['DELETED'])
    context = {
        'supplyreqs_List': supply_reqs,
    }

    return render(request, 'supply_chain/supply_request-deleted.html', context)

# SUPPLY REQUEST ACTIONS MODALS

def update_supplyreqs(request, pk):
    supply_reqs = get_object_or_404(Supply_Request, pk=pk)
    if request.method == 'POST':
        supply_reqs.req_num = request.POST.get('req_num_edit')
        supply_reqs.staff_id = request.POST.get('staff_id_edit')
        supply_reqs.branch_id = request.POST.get('branch_id_edit')
        supply_reqs.date_requested = request.POST.get('date_requested_edit')
        supply_reqs.driver_staff_id = request.POST.get('driver_staff_id_edit')
        supply_reqs.driver_truck = request.POST.get('driver_truck_edit')
        supply_reqs.date_delivered = request.POST.get('date_delivered_edit')
        supply_reqs.save()
        
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def update_supplyreqs_status(request, pk):
    supply_reqs = get_object_or_404(Supply_Request, pk=pk)
    if request.method == 'POST':
        supply_reqs.status = request.POST.get('status_status')
        supply_reqs.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_supplyreqs(request, pk):
    supply_reqs = get_object_or_404(Supply_Request, pk=pk)
    if request.method == 'POST':
        supply_reqs.status = "DELETED"
        supply_reqs.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def recover_supplyreqs(request, pk):
    supply_reqs = get_object_or_404(Supply_Request, pk=pk)
    if request.method == 'POST':
        supply_reqs.status = "ACTIVE"
        supply_reqs.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# SUPPLY CHAIN - PULLOUT REQUEST TABLE

# def pullout_reqList(request):
#     return render(request, 'supply_chain/pullout_request-list.html')









