from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from .models import Location
from .forms import LocationForm

def Home_view(request):
    template_name='base.html'
    context = {}
    return render(request, template_name, context)


def gallary_view(request):
    template_name = 'geoapp/gallery.html'
    context = {}
    return render(request, template_name, context)

def services_view(request):
    template_name = 'geoapp/services.html'
    context = {}
    return render(request, template_name, context)

def contact_view(request):
    template_name = 'geoapp/contact.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url = 'login_url')
def weather_view(request):
    template_name = 'geoapp/index.html'
    context = {}
    return render(request, template_name, context)




# @login_required
def profile_view(request):
    template_name = 'Login&Register/profile.html'
    context = {}
    return render(request, template_name, context)



def Temp_view(request):
    url = 'https://api.weather.gov/gridpoints/TOP/50,50/forecast'
    #city = 'Las Vegas'

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid:
            form.save()

    form = LocationForm()

    

    cities = Location.objects.all()
    weather_data = []

    for city in cities:


        resp = requests.get(url.format(city)).json()

        city_weather = {
                'city':city.city_name,
                'temperature':resp['properties']['periods'][0]['temperature'],
                'name':resp['properties']['periods'][0]['name'],
                'Humidity': resp['properties']['periods'][0]['relativeHumidity']['value'],
                'icon':  resp['properties']['periods'][0]['icon'],
        }

        weather_data.append(city_weather)

    #print(weather_data)




    template_name = 'geoapp/index2.html'
    context = {'city_weather': city_weather, 'form': form}
    return render(request, template_name, context)



