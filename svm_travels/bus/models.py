from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from authentication.models import UserProfile  # adjust import according to your app

class Bus(models.Model):
    image = models.ImageField(upload_to='buss/', null=True, blank=True)
    reg_no = models.CharField(max_length=17)
    no_of_seats = models.IntegerField(default=40, validators=[MaxValueValidator(50)])
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver_bus')

    def __str__(self):
        return f"bus :{self.reg_no} , TotalSeats: {self.no_of_seats}"

    def clean(self):
        """Ensure the assigned driver has UserProfile type 'driver'"""
        try:
            profile = self.driver.profile  # use the related_name
        except UserProfile.DoesNotExist:
            raise ValidationError({'driver': 'Selected user does not have a profile.'})

        if profile.type != 'driver':
            raise ValidationError({'driver': 'Selected user is not registered as a driver.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # run validations before saving
        super().save(*args, **kwargs)
