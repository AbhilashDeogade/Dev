# Generated by Django 4.1.1 on 2023-05-19 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Geolocationapp', '0002_search_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='Humidity',
            field=models.FloatField(null=True),
        ),
    ]
