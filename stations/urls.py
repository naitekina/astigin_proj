from django.urls import path
from .views import *
urlpatterns = [
    path('', view_stations, name='view_stations'),
    path('station/<int:station_id>/details/', view_station_details, name='view_station_details'),
    path('add/', view_add_station, name='view_add_station'),
]

app_name = "stations"