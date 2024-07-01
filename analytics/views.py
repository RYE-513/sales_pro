from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.contrib.sessions.models import Session

class DashboardView(View):
    def get(self, request):
        # count_staff = Session.objects.filter(os_active = 'true').count()
        return render(request, 'analytics/dashboard.html')