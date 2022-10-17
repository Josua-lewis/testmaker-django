import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'layout/home.html', {})

def registration(request):
    return render(request, 'layout/registration.html', {})