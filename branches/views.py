from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from django.http import HttpResponse

from human_resources.models import Staff
from .models import Branches

##########  ##########  BRANCHES  ##########  ##########

# BRANCHES TABLE

def branchList(request):
    branches = Branches.objects.all().order_by('id')
    staff = Staff.objects.all().order_by('id').filter(status='ACTIVE')
    context ={
        'branch_list': branches,
        'staff_list': staff,

    }
    return render(request, 'branches/branches-list.html', context)

# ADD DATA BRANCHES TABLE

def add_branch(request):
    if request.method == 'POST':
        branch_name = request.POST.get('branch_name')
        location = request.POST.get('location')
        staff_id = request.POST.get('staff_id')

        branch = Branches(
            branch_name=branch_name,
            location=location,
            staff_id=staff_id,
        )

        branch.save()
        return redirect('branches:branches')
    
# DELETE DATA BRANCHES TABLE

def deleted_branchList(request):
    branch = Branches.objects.filter(status__in=['DELETED'])
    context = {
        'branch_list': branch,
    }

    return render(request, 'branches/branches-deleted.html', context)

# BRANCHES ACTIONS MODALS

def update_branch(request, pk):
    branch = get_object_or_404(Branches, pk=pk)
    if request.method == 'POST':
        branch.branch_name = request.POST.get('branch_name_edit')
        branch.location = request.POST.get('location_edit')
        branch.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def update_branch_status(request, pk):
    branch = get_object_or_404(Branches, pk=pk)
    if request.method == 'POST':
        branch.status = request.POST.get('status_status')
        branch.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_branch(request, pk):
    branch = get_object_or_404(Branches, pk=pk)
    if request.method == 'POST':
        branch.status = "DELETED"
        branch.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def recover_branch(request, pk):
    branch = get_object_or_404(Branches, pk=pk)
    if request.method == 'POST':
        branch.status = "ACTIVE"
        branch.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
