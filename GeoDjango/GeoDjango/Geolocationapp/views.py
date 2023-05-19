from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Search
from .forms import Search_Location_Form
import folium
import geocoder

# Create your views here.

@login_required(login_url = 'login_url')
def location_view(request):
    if request.method == 'POST':
        form = Search_Location_Form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('location_url')

    else:
        form = Search_Location_Form()

    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your Address is invalid')

    #Cration of Map
    m = folium.Map(location=[19, -12], zoom_start=2)
    
    folium.Marker([lat, lng], tooltip="click for more", popup=country).add_to(m)


    #Html Representaion
    m = m._repr_html_()
    template_name = 'geolocationapp/location.html'
    context = {"m":m, "form": form}
    return render(request, template_name, context)
