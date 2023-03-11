from django.db import models
from schedule.models import Trip


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=5)
    birth_date = models.DateField()
    gender = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return str(self.customer_id) + ': ' + self.first_name + ' ' + self.last_name


class Ticket(models.Model):
    ticket_no = models.IntegerField(primary_key=True)
    date_purchased = models.DateField()
    ticket_cost = models.IntegerField()
    customer = models.ForeignKey(
        Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'

    def __str__(self):
        return f'{self.ticket_no}: {self.customer} '


class TicketTrip(models.Model):
    ticket_trip_id = models.AutoField(primary_key=True)
    ticket_no = models.ForeignKey(
        Ticket, models.DO_NOTHING, db_column='ticket_no', blank=True, null=True)
    trip = models.ForeignKey(Trip, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_trip'

    def __str__(self):
        return f'TRIP: {self.trip} to {self.ticket_no}'
