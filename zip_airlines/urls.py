from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('airplanes.urls')), # redirect to airplane url.py
    path('admin/', admin.site.urls), # unused in this project
]
