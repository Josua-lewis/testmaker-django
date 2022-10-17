from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('signup.html', views.signup, name="signup"),
    path('loginpage.html', views.loginpage, name="login"),
    path('about_us.html', views.about_us, name="about"),


]