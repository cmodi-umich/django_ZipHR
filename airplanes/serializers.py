from rest_framework import serializers
from airplanes.models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    '''
    Serializer to turn model entries into JSON objects with fields: plane_name, id, num_passengers
    '''
    class Meta:
        model = Airplane
        fields = ['plane_name', 'id', 'num_passengers']
