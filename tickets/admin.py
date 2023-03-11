from django.contrib import admin
from .models import Customer, Ticket, TicketTrip

class CustomerAdmin(admin.ModelAdmin):
    model = Customer

class TicketAdmin(admin.ModelAdmin):
    model = Ticket

class TicketTripAdmin(admin.ModelAdmin):
    model = TicketTrip


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Ticket,TicketAdmin)
admin.site.register(TicketTrip,TicketTripAdmin)