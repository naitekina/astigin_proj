from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import TrainDate, Trip
from .forms import AddTrainDate

def view_schedules(request):
    #def get(self, request):
    trips = Trip.objects.all().order_by('trip_date')
    return render(request, 'schedule.html', {'trips': trips, })

def view_add_schedule(request):
    if request.method == 'POST':
        form = AddTrainDate(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            return redirect('/schedule/'+str(new_post.trip_id))
    else:
        form = AddTrainDate()
    return render(request, 'addschedule.html', {'form': form, })

def view_schedule_details(request, trip_id: int, ):
    schedule_details = Trip.objects.get(trip_id = trip_id)
    return render(request, 'schedule_details.html', {'details': schedule_details, })

# def search_schedules(request, origin:str, destination:str):
#     #def get(self, request):
#     trips = Trip.objects.filter(trip_origin = origin).filter(destination = destination)
#     return render(request, 'scheduleSearch.html', {'searched': trips, })

