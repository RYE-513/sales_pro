from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('branches:branches'))

class RegistrationView(View):
    def get(self, request):
        return render(request, 'auth/registration_staff.html')
    
class TenantLoginView(View):
    def get(self, request):
        return render(request, 'auth/tenant_login.html')

class UserProfileView(View):
    def get(self, request):
        return render(request, 'auth/user_profile.html')
        
class DashboardView(View):
    def get(self, request):
        return render(request, 'analytics/dashboard.html')

class SignoutView(View):
    def get(self, request):
        request.session.flush()  # Kill the session
        messages.success(request, "Logged Out Successfully!")
        # Clear all sessions manually
        Session.objects.all().delete()
        return redirect('session:login')

@login_required
def protected_view(request):
    return render(request, 'protected.html') 
