from django import forms
from .models import *

class AddTrain(forms.ModelForm):
    class Meta:
        model = Train
        fields = ['train_id']

        labels = {      
            'train_id' : 'Train:',
        }

    def __init__(self, *args, **kwargs):
        super(AddTrain, self).__init__(*args, **kwargs)

class QueryTrain(forms.ModelForm):
    class Meta:
        model = Train
        #fields = '__all__'
        fields = ['train_id', 'train_model', 'train_maxspeed', 'no_of_seats', 
        'no_of_toilets', 'reclining_seats', 'luggage_storage', 'folding_tables',
        'vending_machines', 'disability_access', 'food_service'
        ]

        labels = {      
            'train_id' : 'Train ID:',
            'train_model' : 'Model:',
            'train_maxspeed' : 'Max Speed (kph):',
            'no_of_seats' : 'No. of Seats:',
            'no_of_toilets' : 'No. of Toilets:',
            'reclining_seats' : 'Reclining Seats:',
            'luggage_storage' : 'Luggage Storage:',
            'folding_tables' : 'Folding Tables',
            'vending_machines' : 'Vending Machines:',
            'disability_access' : 'Disability Access:',
            'food_service' : 'Food Service:',
            #'date' : 'Date:',
        }

    def __init__(self, *args, **kwargs):
        super(QueryTrain, self).__init__(*args, **kwargs)

class QueryMaintenanceWork(forms.ModelForm):
    class Meta:
        model = MaintenanceWork
        #fields = '__all__'
        fields = ['maintenance_id', 'date_maintained', 'maintenance_condition']

        labels = {      
            'maintenance_id' : 'Maintenance ID:',
            'date_maintained' : 'Date:',
            'maintenance_condition' : 'Condition:',
            #'train' : 'Train:',
        }

    def __init__(self, *args, **kwargs):
        super(QueryMaintenanceWork, self).__init__(*args, **kwargs)

class QueryMaintenanceCrew(forms.ModelForm):
    class Meta:
        model = MaintenanceCrew
        fields = '__all__'
        #fields = ['crew_rep', 'task']

        labels = {      
            'crew_id' : 'Crew ID:',
            'crew_rep' : 'Crew in charge:', 
            'task' : 'Tasks:', 
            'maintenance' : 'Maintenance Work:', 
        }

    def __init__(self, *args, **kwargs):
        super(QueryMaintenanceCrew, self).__init__(*args, **kwargs)


