from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about_us, name="about"),
    path('contact/', views.contact_us, name="contact"),
    path('reset/', views.reset_password, name="reset_password"),
    path('forgot/', views.forgot_password, name="forgot_password"),

]