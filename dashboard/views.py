from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')
