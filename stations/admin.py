from django.contrib import admin
from .models import Nodes, Route, Station, StationRoutes, TrainSystem, TripTrainSystem


class NodesAdmin(admin.ModelAdmin):
    model = Nodes


class RouteAdmin(admin.ModelAdmin):
    model = Route


class StationAdmin(admin.ModelAdmin):
    model = Station


class StationRoutesAdmin(admin.ModelAdmin):
    model = StationRoutes


class TrainSystemAdmin(admin.ModelAdmin):
    model = TrainSystem


class TripTrainSystemAdmin(admin.ModelAdmin):
    model = TripTrainSystem


admin.site.register(Nodes, NodesAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(StationRoutes, StationRoutesAdmin)
admin.site.register(TrainSystem, TrainSystemAdmin)
admin.site.register(TripTrainSystem, TripTrainSystemAdmin)
