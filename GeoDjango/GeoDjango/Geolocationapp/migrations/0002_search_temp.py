# Generated by Django 4.1.1 on 2023-05-19 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Geolocationapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='Temp',
            field=models.FloatField(null=True),
        ),
    ]
