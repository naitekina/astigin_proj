from django.db import models
from schedule.models import TrainDate


class Train(models.Model):
    train_id = models.IntegerField(primary_key=True)
    train_model = models.CharField(max_length=255, blank=True, null=True)
    train_maxspeed = models.IntegerField()
    no_of_seats = models.IntegerField()
    no_of_toilets = models.IntegerField(blank=True, null=True)
    reclining_seats = models.IntegerField(blank=True, null=True)
    luggage_storage = models.IntegerField(blank=True, null=True)
    folding_tables = models.IntegerField(blank=True, null=True)
    vending_machines = models.IntegerField(blank=True, null=True)
    disability_access = models.IntegerField(blank=True, null=True)
    food_service = models.IntegerField(blank=True, null=True)
    date = models.ForeignKey(
        TrainDate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train'

    def __str__(self):
        return f'{self.train_id}, MODEL: {self.train_model}'


class MaintenanceWork(models.Model):
    maintenance_id = models.IntegerField(primary_key=True)
    date_maintained = models.DateField(blank=True, null=True)
    maintenance_condition = models.CharField(
        max_length=255, blank=True, null=True)
    train = models.ForeignKey(Train, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_work'

    def __str__(self):
        return f'DATE: {self.date_maintained} | {self.maintenance_id}'


class MaintenanceCrew(models.Model):
    crew_id = models.IntegerField(primary_key=True)
    crew_rep = models.CharField(max_length=255, blank=True, null=True)
    task = models.CharField(max_length=255, blank=True, null=True)
    maintenance = models.ForeignKey(
        MaintenanceWork, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_crew'

    def __str__(self):
        return f'{self.crew_id}: {self.task}'
