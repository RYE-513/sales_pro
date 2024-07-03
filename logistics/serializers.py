from rest_framework import serializers
from .models import Trucks, Drivers

class TrucksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trucks
        fields = '__all__'

class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = '__all__'