from django.urls import path
from airplanes import api
from airplanes import views
from rest_framework.urlpatterns import format_suffix_patterns

'''
Shows which routes activate what 
'''
urlpatterns = [
    path('', views.index), # activates the index html file 
    path('api/', api.airplane_list.as_view()), # activates intitial GET/POST page 
    path('api/<int:pk>/', api.airplane_detail.as_view()), # activates GET/PUT/DELETE page
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])