from django.contrib import admin
from .models import Train, MaintenanceCrew, MaintenanceWork

class TrainAdmin(admin.ModelAdmin):
    model = Train

class MaintenanceCrewAdmin(admin.ModelAdmin):
    model = MaintenanceCrew

class MaintenanceWorkAdmin(admin.ModelAdmin):
    model = MaintenanceWork

admin.site.register(Train,TrainAdmin)
admin.site.register(MaintenanceCrew,MaintenanceCrewAdmin)
admin.site.register(MaintenanceWork,MaintenanceWorkAdmin)