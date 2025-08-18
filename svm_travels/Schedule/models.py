from django.db import models
from bus.models import Bus
from BusRoute.models import BusRoute
# Create your models here.


class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete= models.CASCADE)
    busroute = models.ForeignKey(BusRoute, on_delete= models.CASCADE)
    start_time = models.DateTimeField()

    def __str__(self):
        return f"schedule bus {self.bus}, {self.busroute} at {self.start_time}"