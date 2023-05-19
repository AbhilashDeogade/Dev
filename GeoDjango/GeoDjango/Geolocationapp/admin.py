from django.contrib import admin
from .models import Search

@admin.register(Search)
class CityAdmin(admin.ModelAdmin):
    list_display=['address', 'date', 'Temp', 'Humidity']
