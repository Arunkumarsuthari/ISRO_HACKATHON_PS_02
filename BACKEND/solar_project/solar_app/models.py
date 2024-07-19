from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Building(models.Model):
    name = models.CharField(max_length=255)
    location = models.PolygonField()
    rooftop_area = models.FloatField()
    solar_potential = models.FloatField()

class SolarData(models.Model):
    date = models.DateField()
    radiation = models.FloatField()
    location = models.PointField()
