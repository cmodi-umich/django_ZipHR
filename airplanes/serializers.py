from rest_framework import serializers
from airplanes.models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ['plane_name', 'id', 'num_passengers']
