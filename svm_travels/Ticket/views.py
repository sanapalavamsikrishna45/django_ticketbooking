from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView
from django.urls import reverse
from .models import Ticket, Passenger
from .forms import TicketCreateForm
from Schedule.models import Schedule
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class BookTicketView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'book_ticket.html'
    form_class = TicketCreateForm

    def get_success_url(self):
        return reverse('confirm_ticket', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedule_id = self.kwargs.get('schedule_id')
        this_schedule = get_object_or_404(Schedule, id=schedule_id)
        context['schedule'] = this_schedule
        return context

    def form_valid(self, form):
        schedule_id = self.kwargs.get('schedule_id')
        this_schedule = get_object_or_404(Schedule, id=schedule_id)
        form.instance.schedule = this_schedule

        # Save ticket first (required for ManyToMany)
        response = super().form_valid(form)

        # Handle passengers: get list of passenger IDs from POST
        passenger_ids = self.request.POST.getlist('passengers')  # multi-select field
        passengers = Passenger.objects.filter(id__in=passenger_ids)
        self.object.passengers.set(passengers)

        # Calculate ticket amount
        self.object.amount = this_schedule.busroute.price * passengers.count()
        self.object.save()

        return response



class ConfirmTicketView(DetailView):
    model = Ticket
    template_name = 'confirm_ticket.html'
    context_object_name = 'ticket'

