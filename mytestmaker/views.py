import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'layout/home.html', {})

def signup(request):
    return render(request, 'layout/signup.html', {})

def loginpage(request):
    return render(request, 'layout/loginpage.html', {})

def about_us(request):
    return render(request, 'layout/about_us.html', {})

def contact_us(request):
    return render(request, 'layout/contact_us.html', {})