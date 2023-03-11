from django import forms
from .models import Customer, Ticket, TicketTrip

class AddTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_no']

        labels = {      
            'ticket_no' : 'Ticket:',
        }

    def __init__(self, *args, **kwargs):
        super(AddTicket, self).__init__(*args, **kwargs)

