from django.db import models
from mainapp.models import Stop
# Create your models here.
from django.core.exceptions import ValidationError


class BusRoute(models.Model):
    start = models.ForeignKey(Stop, on_delete = models.CASCADE, related_name = 'route_start')
    end = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name = 'route_end')
    dist = models.IntegerField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"BusRoute From {self.start} To {self.end}"
    
    def clean(self):
        if self.start == self.end:
            raise ValidationError("Start and End stops cannot be the same.")