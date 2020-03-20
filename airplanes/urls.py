from django.urls import path
from airplanes import api
from airplanes import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index), 
    path('api/', api.airplane_list.as_view()),
    path('api/<int:pk>/', api.airplane_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])