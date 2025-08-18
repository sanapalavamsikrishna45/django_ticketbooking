from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Create your views here.
from .models import BusRoute

from django.urls import reverse_lazy

# def routeView(request):
#     template = 'home.html'
#     context={
#         'busroutes' : BusRoute.objects.all()

#     }
#     return render (request,template,context)

class RouteList(ListView):
    model = BusRoute
    template_name = 'busroute.html'
    context_object_name ='busroutes'


class AddRoute(CreateView):
    model = BusRoute
    template_name = 'addroute.html'
    fields = '__all__'
    success_url = reverse_lazy('route_page')


class UpdateRoute(UpdateView):
    model = BusRoute
    template_name = 'updateroute.html'
    fields = "__all__"
    success_url = reverse_lazy('route_page')

    

class DeleteRoute(DeleteView):
    model = BusRoute
    template_name = 'deleteroute.html'
    success_url = reverse_lazy('route_page')
    



