from django.urls import path
from .views import *

urlpatterns = [
    path('', view_schedules, name='view_schedules'),
    path('<int:trip_id>/details/', view_schedule_details, name='view_schedule_details'),
    path('add/', view_add_schedule, name='view_add_schedule'),
  #  path('<str:trip_origin>/str:<trip_destination>')
]

app_name = "schedule"