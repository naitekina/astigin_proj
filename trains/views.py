from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
import datetime

def view_trains(request):
    train = Train.objects.all()
    # form_train = QueryTrain(request.POST or None)  
    # form_maintenancework = QueryMaintenanceWork(request.POST or None)  
    # form_maintenancecrew = QueryMaintenanceCrew(request.POST or None)  
    # queryset_train = Train.objects.all()
    # queryset_maintenancework = MaintenanceWork.objects.all()
    # queryset_maintenancecrew = MaintenanceCrew.objects.all()

    # context = {
    #     'train': train,
    #     'form_train': form_train,
    #     'form_maintenancework': form_maintenancework,
    #     'form_maintenancecrew': form_maintenancecrew,
    #     'queryset_train': queryset_train,
    #     'queryset_maintenancework': queryset_maintenancework,
    #     'queryset_maintenancecrew': queryset_maintenancecrew,
    # }

    # if request.method == 'POST':
    #     queryset_train = Train.objects.filter(
    #         train_id__icontains=form_train['train_id'].value(),
    #         train_model__icontains=form_train['train_model'].value(),
    #         train_maxspeed__icontains=form_train['train_maxspeed'].value(),
    #         no_of_seats__icontains=form_train['no_of_seats'].value(),
    #         no_of_toilets__icontains=form_train['no_of_toilets'].value(),
    #         reclining_seats__icontains=form_train['reclining_seats'].value(),
    #         luggage_storage__icontains=form_train['luggage_storage'].value(),
    #         folding_tables__icontains=form_train['folding_tables'].value(),
    #         vending_machines__icontains=form_train['vending_machines'].value(),
    #         disability_access__icontains=form_train['disability_access'].value(),
    #         food_service__icontains=form_train['food_service'].value()
    #     )
    
    #     queryset_maintenancework = MaintenanceWork.objects.filter(#crew_id__icontains=form['crew_id'].value(),
    #         maintenance_id__icontains=form_maintenancework['maintenance_id'].value(),
    #         date_maintained__icontains=form_maintenancework['date_maintained'].value(),
    #         maintenance_condition__icontains=form_maintenancework['maintenance_condition'].value(),
    #         #train__icontains=form_maintenancework['train'].value()
    #     )

    #     queryset_maintenancecrew = MaintenanceCrew.objects.filter(#crew_id__icontains=form['crew_id'].value(),
    #         crew_id__icontains=form_maintenancecrew['crew_id'].value(),
    #         crew_rep__icontains=form_maintenancecrew['crew_rep'].value(),
    #         task__icontains=form_maintenancecrew['task'].value(),
    #         #maintenance__icontains=form_maintenancecrew['maintenance'].value(),
    #     )

    #     context = {
    #         'train': train,
    #         'form_train': form_train,
    #         'form_maintenancework': form_maintenancework,
    #         'form_maintenancecrew': form_maintenancecrew,
    #         'queryset_train': queryset_train,
    #         'queryset_maintenancework': queryset_maintenancework,
    #         'queryset_maintenancecrew': queryset_maintenancecrew,
    #     }

    return render(request, 'trains.html', {'train':train})

def view_add_train(request):
    if request.method == 'POST':
        form = AddTrain(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            return redirect('/train/'+str(new_post.train_id))
    else:
        form = AddTrain()
    return render(request, 'addtrain.html', {'form': form, })

def view_train_details(request):
    train_details = Train.objects.all()
    return render(request, 'train.html', {'train_details': train_details, })

def showMaintenance(request):
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 5, 1)
    maintenance_details = MaintenanceWork.objects.filter(
        Q(date_maintained__range=[start_date,end_date])
    ).order_by('date_maintained')
    return render(request, 'trains.html', {'m_details': maintenance_details, })
