from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Building, SolarData
from .serializers import BuildingSerializer, SolarDataSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class SolarDataViewSet(viewsets.ModelViewSet):
    queryset = SolarData.objects.all()
    serializer_class = SolarDataSerializer
