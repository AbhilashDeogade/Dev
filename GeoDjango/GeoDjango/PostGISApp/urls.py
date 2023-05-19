from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.Home_view, name='home_url'),
    path('gallery/', views.gallary_view, name='gallery_url'),
    path('services/', views.services_view, name='services_url'),
    path('contact/', views.contact_view, name='contact_url'),
    path('profile/', views.profile_view, name='profile_url'),
    path('temp/', views.Temp_view, name='temp_url'),
    path('weather/', views.weather_view, name='weather_url'),
    
    
    
]