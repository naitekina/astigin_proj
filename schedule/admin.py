from django.contrib import admin
from .models import TrainDate, Trip

class TrainDateAdmin(admin.ModelAdmin):
    model = TrainDate

class TripAdmin(admin.ModelAdmin):
    model = Trip

admin.site.register(TrainDate,TrainDateAdmin)
admin.site.register(Trip,TripAdmin)