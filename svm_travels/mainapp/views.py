from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Stop
# Create your views here.
def homeView(request):
    template = 'home.html'
    context = {
        'stops' : Stop.objects.all()
        
    }
    return render(request, template, context)


class StopList(ListView):
    model = Stop
    template_name = 'stops.html'
    context_object_name = 'stops'