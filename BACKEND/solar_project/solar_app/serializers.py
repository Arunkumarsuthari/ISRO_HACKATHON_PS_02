from rest_framework import serializers
from .models import Building, SolarData

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class SolarDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarData
        fields = '__all__'
