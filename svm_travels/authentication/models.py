from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone

from datetime import timedelta

class EmailOTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length = 6)
    created_at = models.DateTimeField(auto_now_add = True)


    def is_expired(self):
        return timezone.now()>self.created_at +timedelta(minutes = 10)

    def __str__(self):
        return f"{self.email} - {self.otp}"



class UserProfile(models.Model):
    USER_TYPES = [
        ('driver', 'Driver'),
        ('customer', 'Customer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    type = models.CharField(max_length=10, choices=USER_TYPES, default='customer')

    def __str__(self):
        return f"{self.user.username} - {self.type}"