from django.db import models

class Location(models.Model):
    city_name = models.CharField(max_length=250)
    Temp = models.FloatField(null=True,)
    
    

    def __str__(self):
        return self.city_name
