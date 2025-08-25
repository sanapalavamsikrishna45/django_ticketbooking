from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from Schedule.models import Schedule
from mainapp.models import Stop


class Passenger(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.ForeignKey(  # 🔹 optional: link passengers to their owner
        User,
        on_delete=models.CASCADE,
        related_name="passengers",
        null=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.age}, {self.get_gender_display()})"


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # start = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='ticket_start_stop')
    # end = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='ticket_end_stop')
    booking_date = models.DateField()
    amount = models.PositiveIntegerField(default=0)
    passengers = models.ManyToManyField(Passenger, related_name="tickets")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.get_status_display()}"

    @property
    def passenger_count(self):
        return self.passengers.count()
