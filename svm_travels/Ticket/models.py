from django.db import models

# Create your models here.
from Schedule.models import Schedule
from mainapp.models import Stop
from django.core.exceptions import ValidationError


# class TicketStatus(models.TextChoices):
#     PENDING = 'pending','pending'
#     CONFIRMED = 'Confirmed', 'Confirmed'
#     CANCELLED = 'Cancelled', 'Cancelled'

class Ticket(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete= models.CASCADE)
    start = models.ForeignKey(Stop, on_delete= models.CASCADE, related_name= 'ticket_start_stop')
    end = models.ForeignKey(Stop, on_delete= models.CASCADE, related_name= 'ticket_end_stop')
    booking_date = models.DateTimeField()
    amount = models.PositiveIntegerField()
    passengers = models.PositiveIntegerField(default=0)
    status = models.CharField( max_length=20, choices=[
        ('Pending','pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')
    booked_at = models.DateTimeField(auto_now_add=True)


    def clean(self):
        if self.start_id == self.end_id:
            raise ValidationError("Start and End stops cannot be the same.")
        


    def __str__(self):
        return f"Ticket Status {self.id} -{self.get_status_display()}"