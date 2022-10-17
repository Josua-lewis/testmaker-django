import re
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'layout/home.html', {})

def signup(request):
    return render(request, 'layout/signup.html', {})

def loginpage(request):
    return render(request, 'layout/loginpage.html', {})