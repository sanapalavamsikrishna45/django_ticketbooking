from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Bus(models.Model):
    image = models.ImageField(upload_to='buss/', null = True, blank = True)
    reg_no = models.CharField(max_length=17)
    no_of_seats = models.IntegerField(default=40, validators = [
        MaxValueValidator(50)
    ])



    def __str__(self):
        return f"bus :{self.reg_no} , TotalSeats: {self.no_of_seats}"
