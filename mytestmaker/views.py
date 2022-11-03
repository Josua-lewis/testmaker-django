import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def register(request):
    return render(request, 'register.html', {})

def loginpage(request):
    return render(request, 'loginpage.html', {})

def about_us(request):
    return render(request, 'about_us.html', {})

def contact_us(request):
    return render(request, 'contact_us.html', {})