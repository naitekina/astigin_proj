from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Nodes, Route, Station, StationRoutes, TrainSystem, TripTrainSystem
from .forms import AddStation


def view_stations(request):
    train_systems = TrainSystem.objects.all()
    stations = Station.objects.filter(train_system__contains="Taguig")
    return render(request, 'stations.html', {'train_systems': train_systems, 'stations': stations, })


def view_add_station(request):
    if request.method == 'POST':
        form = AddStation(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            return redirect('/station/'+str(new_post.station_id))
    else:
        form = AddStation()
    return render(request, 'addstation.html', {'form': form, })


def view_station_details(request):
    station_details = Station.objects.all()
    return render(request, 'station.html', {'station_details': station_details, })
