from django.urls import path
from .views import *

urlpatterns = [
    path('', view_tickets, name='view_tickets'),
    path('ticket/<int:ticket_no>/details/', view_ticket_details, name='view_ticket_details'),
    path('add/', view_add_ticket, name='view_add_ticket'),
]

app_name = "tickets"