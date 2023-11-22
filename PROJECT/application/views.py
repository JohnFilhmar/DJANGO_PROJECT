# myapp/views.py
from django.shortcuts import render

def login(request):
    print(request.GET)
    return render(request, 'login.html')

def register(request):
    print(request.GET)
    return render(request, 'register.html')

def dashboard(request):
    print(request.GET)
    return render(request, 'dashboard.html')

def form(request):
    print(request.GET)
    return render(request, 'appointment.html')

def patient(request):
    print(request.GET)
    return render(request, 'patient.html')

def patient(request):
    print(request.GET)
    return render(request, 'patient.html')

def records(request):
    print(request.GET)
    return render(request, 'records.html')

def inventory(request):
    print(request.GET)
    return render(request, 'inventory.html')