from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginpage, name="login"),
    path('about/', views.about_us, name="about"),
    path('contact/', views.contact_us, name="contact"),


]