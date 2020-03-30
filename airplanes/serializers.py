from rest_framework import serializers
from airplanes.models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    '''
    Serializer to turn model entries into JSON objects with fields: plane_name, id, num_passengers
    '''

    def validate_id(self, value):
        if value > 10:
            raise serializers.ValidationError("Max number of planes reached")
        return value

    def validate(self, data):
        data = super().validate(data)
        temp_plane = Airplane(id=data["id"], num_passengers=data["num_passengers"])
        if temp_plane.max_minutes() > 20:
            raise serializers.ValidationError("Too many passengers")
        return data
        

    class Meta:
        model = Airplane
        fields = ['plane_name', 'id', 'num_passengers']
