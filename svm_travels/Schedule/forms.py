from django import forms
from .models import Schedule

class HTML5DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

        widgets = {
            'start_time' : HTML5DateTimeInput()
        }