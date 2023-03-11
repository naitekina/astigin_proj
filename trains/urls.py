from django.urls import path
from .views import *

urlpatterns = [
    path('', showMaintenance, name='showMaintenance'),
    path('train/<int:train_id>/details/', view_train_details, name='view_train_details'),
    path('add/', view_add_train, name='view_add_train'),
]

app_name = "trains"