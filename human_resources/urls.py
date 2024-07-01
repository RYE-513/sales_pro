from django.urls import path
from . import views

app_name = 'human_resources'

urlpatterns = [

	# ROLES

    path('roles/', views.roleList, name='roles'),    
    path('add_roles/', views.add_roles, name='add_roles'),
    
    path('update_role/<int:pk>/', views.update_role, name='update_role'),
    path('delete_role/<int:pk>/', views.delete_role, name='delete_role'),
    path('recover_role/<int:pk>/', views.recover_role, name='recover_role'),

    # STAFF

    path('staff/', views.staffList, name='staff'),
    path('add_staff/', views.add_staff, name='add_staff'),

    path('update_staff/<int:pk>/', views.update_staff, name='update_staff'),
    path('update_staff_status/<int:pk>/', views.update_staff_status, name='update_staff_status'),
    path('delete_staff/<int:pk>/', views.delete_staff, name='delete_staff'),
    path('recover_staff/<int:pk>/', views.recover_staff, name='recover_staff'),

    # DELETED HUMAN RESOURCES

    path('deleted_staffList/', views.deleted_staffList, name='deleted_staffList'),
    path('deleted_roleList/', views.deleted_roleList, name='deleted_roleList'),


]
