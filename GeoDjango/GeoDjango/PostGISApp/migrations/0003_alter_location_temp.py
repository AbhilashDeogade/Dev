# Generated by Django 4.1.1 on 2023-05-19 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostGISApp', '0002_location_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='Temp',
            field=models.FloatField(null=True),
        ),
    ]