from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Roles, Staff

##########  ##########  ROLES  ##########  ##########

# ROLES TABLE

def roleList(request):
    role = Roles.objects.filter(status__in=['ACTIVE'])
    context = {
        'role_list': role,
    }
    return render(request, 'human_resources/roles-list.html', context)

# ADD DATA ROLES TABLE

def add_roles(request):
    if request.method == 'POST':
        role_name = request.POST.get('role_name')
        description = request.POST.get('description')
        roles = Roles(
            role_name = role_name,
            description = description,
        )
        roles.save()
    return redirect('human_resources:roles')

# DELETE DATA ROLES TABLE

def deleted_roleList(request):
    role = Roles.objects.filter(status__in=['DELETED'])
    context = {
        'role_list': role,
    }
    return render(request, 'human_resources/roles-deleted.html', context)
    
# ROLES ACTIONS MODALS

def update_role(request, pk):
    role = get_object_or_404(Roles, pk=pk)
    if request.method == 'POST':
        role.role_name = request.POST.get('role_name_edit')
        role.description = request.POST.get('description_edit')
        role.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_role(request, pk):
    role = get_object_or_404(Roles, pk=pk)
    if request.method == 'POST':
        role.status = "DELETED"
        role.save()
        return JsonResponse({'status': 'success'})
        # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def recover_role(request, pk):
    role = get_object_or_404(Roles, pk=pk)
    if request.method == 'POST':
        role.status = "ACTIVE"
        role.save()
        return JsonResponse({'status': 'success'})
        # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


##########  ##########  STAFF  ##########  ##########

# STAFF TABLE

def staffList(request):
    staff = Staff.objects.all().order_by('id')
    role = Roles.objects.filter(status__in=['ACTIVE'])
    context ={
        'staff_list': staff,
        'role_list': role,
    }
    return render(request, 'human_resources/staff-list.html', context)

# ADD DATA STAFF TABLE

def add_staff(request):
    if request.method == 'POST':
        first_name  = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email')
        role_id = request.POST.get('role_id')
        staff = Staff(
            first_name = first_name,
            last_name = last_name,
            mobile_no = mobile_no,
            email = email,
            role_id = role_id
        )
        staff.save()
    return redirect('human_resources:staff')

# DELETE DATA STAFF TABLE

def deleted_staffList(request):
    staff = Staff.objects.all().order_by('id')
    context ={
        'staff_list': staff,
    }
    return render(request, 'human_resources/staff-deleted.html', context)

# STAFF ACTIONS MODALS

def update_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.first_name = request.POST.get('first_name_edit')
        staff.last_name = request.POST.get('last_name_edit')
        staff.mobile_no = request.POST.get('mobile_no_edit')
        staff.email = request.POST.get('email_edit')
        staff.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def update_staff_status(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.status = request.POST.get('status_status')
        staff.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def delete_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.status = "DELETED"
        staff.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def recover_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.status = "ACTIVE"
        staff.save()
        return JsonResponse({'status': 'success'})
    # Handle other HTTP methods or provide a response for non-POST requests
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



