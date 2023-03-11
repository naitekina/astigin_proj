from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Customer, Ticket, TicketTrip
from .forms import AddTicket

def view_tickets(request):
    customer = Customer.objects.filter(
        last_name__startswith="S"
    )

    ticket = Ticket.objects.all()
    return render(request, 'tickets.html', {'ticket': ticket, 'customer': customer})

def view_add_ticket(request):
    if request.method == 'POST':
        form = AddTicket(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save()
            return redirect('/ticket/'+str(new_post.ticket_no))
    else:
        form = AddTicket()
    return render(request, 'addticket.html', {'form': form, })

def view_ticket_details(request):
    ticket_details = Ticket.objects.all()
    return render(request, 'ticket.html', {'ticket_details': ticket_details, })

