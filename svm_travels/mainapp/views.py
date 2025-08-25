from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Stop
from django.urls import reverse_lazy

# Create your views here.
from django.shortcuts import render
from Schedule.models import Schedule
from mainapp.models import Stop

def homeView(request):
    stops = Stop.objects.all()
    schedules = None

    start = request.GET.get('start', '').strip()
    end = request.GET.get('end', '').strip()

    if start or end:
        schedules = Schedule.objects.all()
        if start:
            schedules = schedules.filter(busroute__start__icontains=start)
        if end:
            schedules = schedules.filter(busroute__end__icontains=end)

    context = {
        'stops': stops,
        'schedules': schedules,
        'start': start,
        'end': end,
    }
    return render(request, 'home.html', context)



class StopList(ListView):
    model = Stop
    template_name = 'stops.html'
    context_object_name = 'stops'

class AddStop(CreateView):
    model = Stop
    template_name = 'addstop.html'
    fields = '__all__'
    success_url = reverse_lazy('stops_page')

class UpdateProduct(UpdateView):
    model = Stop
    template_name = 'updatestop.html'
    fields = '__all__'
    success_url = reverse_lazy('stops_page')

class DeleteStop(DeleteView):
    model = Stop
    template_name = 'deletestop.html'
    success_url = reverse_lazy('stops_page')

# class DetailStop(DetailView):
#     model = Stop
#     template_name = 