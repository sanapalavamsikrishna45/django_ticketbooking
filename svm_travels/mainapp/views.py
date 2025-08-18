from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Stop
from django.urls import reverse_lazy

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