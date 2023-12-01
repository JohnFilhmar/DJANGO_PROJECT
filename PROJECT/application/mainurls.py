from xml.etree.ElementInclude import include
from django.urls import path
from .views import login, register, dashboard, form, patient, records, inventory, appointment

urlpatterns = [
    path('', dashboard, name='dashboard'),  # Add this line for the empty path
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('form/', form, name='form'),
    path('appointment/',appointment, name='appointment'),
    path('patient/', patient, name='patient'),
    path('records/', records, name='records'),
    path('inventory/', inventory, name='inventory'),
    
]