from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from airplanes.models import Airplane
from airplanes.serializers import AirplaneSerializer
import json


class airplane_list(APIView):
    """
    List all airplanes, or create a new airplane.
    """
    def get(self, request, format=None):
        airplanes = Airplane.objects.all()
        serializer = AirplaneSerializer(airplanes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AirplaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class airplane_detail(APIView):
    """
    Retrieve, update or delete an airplane.
    """
    def get_object(self, pk):
        try:
            return Airplane.objects.get(pk=pk)
        except Airplane.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        airplane = self.get_object(pk)
        serializer = AirplaneSerializer(airplane)
        data = serializer.data
        data['fuel_capacity'] = airplane.fuel_capacity()
        data['fuel_consumption'] = airplane.fuel_consumption()
        data['max_minutes'] = airplane.max_minutes()
        return Response(data)

    def put(self, request, pk, format=None):
        airplane = self.get_object(pk)
        serializer = AirplaneSerializer(airplane, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        airplane = self.get_object(pk)
        airplane.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

