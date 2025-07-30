from django.db import models

# Create your models here.

class Stop(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length= 200)
    long = models. DecimalField(max_digits=10, decimal_places=8)
    lati = models.DecimalField(max_digits=10, decimal_places=8)
    
    def __str__(self):
        return f"Stop : {self.name} in {self.state}."
