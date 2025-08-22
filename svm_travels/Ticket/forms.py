from django import forms


from .models import Ticket

class HTML5DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class TicketCreateForm(forms.ModelForm):
    class Meta :
        model = Ticket
        fields = ['passengers', 'booking_date']

        widgets = {
            'booking_date' :HTML5DateTimeInput()
        }
