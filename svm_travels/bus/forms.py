from django import forms

from .models import Bus
from authentication.models import UserProfile
from django.contrib.auth.models import User 

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        driver_profiles = UserProfile.objects.filter(type='driver').values_list('user_id', flat=True)
        self.fields['driver'].queryset = User.objects.filter(id__in=driver_profiles)

