from django.db import models

class TrainDate(models.Model):
    date_id = models.IntegerField(primary_key=True)
    trip_sched = models.DateField()

    class Meta:
        managed = False
        db_table = 'train_date'

    def __str__(self):
        return self.trip_sched
        
class Trip(models.Model):
    # Field name made lowercase.
    trip_id = models.IntegerField(db_column='trip_ID', primary_key=True)
    trip_departure = models.DateTimeField()
    trip_arrival = models.DateTimeField()
    trip_duration = models.CharField(max_length=30)
    trip_cost = models.IntegerField()
    trip_date = models.ForeignKey(
        TrainDate, models.DO_NOTHING, blank=True, null=True)
    trip_origin = models.CharField(max_length=30)
    trip_destination = models.CharField(max_length=30)
    
    class Meta:
        managed = False
        db_table = 'trip'

    def __str__(self):
        return str(self.trip_id) + ': ' + str(self.trip_origin) + '-' + str(self.trip_destination)

