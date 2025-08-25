from django import forms
from .models import Schedule

class HTML5DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class ScheduleCreateForm(forms.ModelForm):
    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={'type': 'time'}
        ),
        input_formats=['%H:%M'],
    )

    class Meta:
        model = Schedule
        fields = '__all__'