from django.http import HttpResponse
from .api import airplane_list, airplane_detail
from .models import Airplane
from django.shortcuts import render


def index(request):
    airplanes_list = Airplane.objects.all()
    context = {'airplanes_list': airplanes_list}
    return render(request, 'airplanes/index.html', context)