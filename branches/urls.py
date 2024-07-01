from django.urls import path
from . import views

app_name = 'branches'

urlpatterns = [

    path('branches/', views.branchList, name='branches'),
    path('add_branch/', views.add_branch, name='add_branch'),

    path('update_branch/<int:pk>/', views.update_branch, name='update_branch'),
    path('update_branch_status/<int:pk>/', views.update_branch_status, name='update_branch_status'),
    path('delete_branch/<int:pk>/', views.delete_branch, name='delete_branch'),
    path('recover_branch/<int:pk>/', views.recover_branch, name='recover_branch'),

    # DELETED BRANCHES

    path('deleted_branchList/', views.deleted_branchList, name='deleted_branchList'),

]
