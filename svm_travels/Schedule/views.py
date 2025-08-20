from django.shortcuts import render
from .forms import ScheduleCreateForm
# Create your views here.
from .models import Schedule
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

class ScheduleList(ListView):
    model = Schedule
    template_name = 'schedule.html'
    context_object_name ='schedules'



class AddSchedule(CreateView):
    model = Schedule
    template_name = 'addschedule.html'
    form_class = ScheduleCreateForm
    success_url = reverse_lazy('schedule_page')


class UpdateSchedule(UpdateView):
    model = Schedule
    template_name = 'updateschedule.html'
    fields = '__all__'
    success_url = reverse_lazy('schedule_page')


class DeleteSchedule(DeleteView):
    model = Schedule
    template_name = 'deleteschedule.html'
    success_url = reverse_lazy('schedule_page')