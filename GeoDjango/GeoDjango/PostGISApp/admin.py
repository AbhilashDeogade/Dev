from django.contrib import admin
from .models import Location

@admin.register(Location)
class CityAdmin(admin.ModelAdmin):
    list_display=['city_name', 'Temp']

