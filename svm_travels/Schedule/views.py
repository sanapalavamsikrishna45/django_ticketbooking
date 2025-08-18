from django.shortcuts import render

# Create your views here.
from .models import Schedule
from django.views.generic import CreateView, ListView, DeleteView, UpdateView


class ScheduleList(ListView):
    model = Schedule
    template_name = 'schedule.html'
    context_object_name ='schedules'
