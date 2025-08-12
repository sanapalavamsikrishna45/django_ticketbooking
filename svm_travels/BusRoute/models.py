from django.db import models
from mainapp.models import Stop
# Create your models here.



class BusRoute(models.Model):
    start = models.ForeignKey(Stop, on_delete = models.CASCADE, related_name = 'route_start')
    end = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name = 'route_end')
    dist = models.IntegerField()

    def __str__(self):
        return f"BusRoute From {self.start} To {self.end}"