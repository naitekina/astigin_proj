from django import forms
from .models import TrainDate, Trip

class AddTrainDate(forms.ModelForm):
    class Meta:
        model = TrainDate
        fields = ['trip_sched']

        labels = {      
            'trip_sched' : 'Trip schedule:',
        }

    def __init__(self, *args, **kwargs):
        super(AddTrainDate, self).__init__(*args, **kwargs)
        #self.fields['assignment_image'].required = False

