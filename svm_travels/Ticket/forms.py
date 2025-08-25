from django import forms
from .models import Ticket, Passenger
import datetime

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['booking_date', 'passengers']  # schedule and amount handled in view
        widgets = {
            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': datetime.date.today().strftime('%Y-%m-%d')  # ensures min date is today
                }
            ),
            'passengers': forms.CheckboxSelectMultiple(),  # multiple passengers as checkboxes
        }

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'gender', 'age']
