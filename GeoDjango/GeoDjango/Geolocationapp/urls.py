from django.urls import path
from .import views

urlpatterns = [
    path('location/', views.location_view, name='location_url'),
   
]