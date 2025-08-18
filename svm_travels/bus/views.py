from django.shortcuts import render
from .models import Bus
# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
# def busView(request):
#     template= 'home.html'
#     context = {
#         'buss' : Bus.objects.all()
#     }
#     return render (request, template, context)


class BusList(ListView):
    model=Bus
    template_name = 'bus.html'
    context_object_name = 'buses'



class AddBus(CreateView):
    model = Bus
    template_name = 'addbus.html'
    fields = '__all__'
    success_url = reverse_lazy('bus_page')


class UpdateBus(UpdateView):
    model = Bus
    template_name = 'updatebus.html'
    fields = '__all__'
    success_url = reverse_lazy('bus_page')



class DeleteBus(DeleteView):
    model = Bus
    template_name = 'deletebus.html'
    success_url = reverse_lazy('bus_page')