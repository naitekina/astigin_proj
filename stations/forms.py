from django import forms
from .models import Nodes, Route, Station, StationRoutes, TrainSystem, TripTrainSystem


class AddStation(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['station_id']

        labels = {
            'station_id': 'Station:',
        }

    def __init__(self, *args, **kwargs):
        super(AddStation, self).__init__(*args, **kwargs)
