from django.db import models
from schedule.models import Trip


class Nodes(models.Model):
    # Field name made lowercase.
    node_id = models.IntegerField(db_column='node_ID', primary_key=True)
    # Field name made lowercase.
    connected_station_id_1 = models.IntegerField(
        db_column='connected_station_ID_1', blank=True, null=True)
    connected_station_1_duration = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    connected_station_id_2 = models.IntegerField(
        db_column='connected_station_ID_2', blank=True, null=True)
    connected_station_2_duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodes'

    def __str__(self):
        return str(self.connected_station_id_1) + ' - ' + str(self.connected_station_id_2)

class Station(models.Model):
    # Field name made lowercase.
    station_id = models.IntegerField(db_column='station_ID', primary_key=True)
    station_name = models.CharField(max_length=100, blank=True, null=True)
    train_system = models.CharField(max_length=30, blank=True, null=True)
    one_way = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    node = models.ForeignKey(Nodes, models.DO_NOTHING,
                             db_column='node_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'

    def __str__(self):
        return str(self.station_id) + ': ' + self.train_system

class Route(models.Model):
    route_id = models.IntegerField(primary_key=True)
    route_start = models.CharField(max_length=30, blank=True, null=True)
    route_end = models.CharField(max_length=30, blank=True, null=True)
    route_cost = models.IntegerField()
    route_duration = models.CharField(max_length=30)
    route_type = models.CharField(max_length=10)
    one_way = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'

    def __str__(self):
        return self.route_type + ': ' + str(self.route_start) + '-' + str(self.route_end)



class StationRoutes(models.Model):
    station_routes_id = models.AutoField(primary_key=True)
    # Field name made lowercase.
    station = models.OneToOneField(
        Station, models.DO_NOTHING, db_column='station_ID', blank=True, null=True)
    route = models.OneToOneField(
        Route, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station_routes'

    def __str__(self):
        return f'STATION: {self.station} is part of ROUTE: {self.route}'


class TrainSystem(models.Model):
    # Field name made lowercase.
    train_system_id = models.IntegerField(
        db_column='train_system_ID', primary_key=True)
    system_name = models.CharField(max_length=100, blank=True, null=True)
    system_type = models.CharField(max_length=30, blank=True, null=True)
    train_system_cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'train_system'

    def __str__(self):
        return self.system_name


class TripTrainSystem(models.Model):
    train_trip_id = models.AutoField(primary_key=True)
    # Field name made lowercase.
    trip = models.OneToOneField(
        Trip, models.DO_NOTHING, db_column='trip_ID', blank=True, null=True)
    # Field name made lowercase.
    train_system = models.OneToOneField(
        TrainSystem, models.DO_NOTHING, db_column='train_system_ID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trip_train_system'

    def __str__(self):
        return f'TRIP: {self.trip} is in TRAIN SYSTEM: {self.train_system}'
