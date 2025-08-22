from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .forms import TicketCreateForm
# Create your views here.
from django.urls import reverse_lazy, reverse
from .models import Ticket

from Schedule.models import Schedule


class BookTicketView(CreateView):
    model = Ticket
    template_name = 'book_ticket.html'
    # context_object_name = 'ticket'
    form_class = TicketCreateForm
    # success_url = reverse('confirm_ticket')

    def get_success_url(self):
        # Dynamically build URL to confirmation page with new ticket ID
        return reverse('confirm_ticket', kwargs={'pk': self.object.pk})
    
    # def get_initial(self):
    #     initial = super().get_initial()
    #     # Access the 'parent_id' from URL kwargs
    #     schedule_id = self.kwargs.get('schedule_id')
    #     schedule = Schedule.objects.get(id = schedule_id)
    #     if schedule:
    #         initial['schedule'] = schedule  # Set an initial value for a form field
    #     return initial
    def get_context_data(self, **kwargs):
        schedule_id = self.kwargs.get('schedule_id')
        this_schedule = Schedule.objects.get(id = schedule_id)

        context = super().get_context_data(**kwargs)
        context['schedule'] = this_schedule
        return context

    def form_valid(self, form):
        # Access the 'parent_id' here if needed for saving logic
        schedule_id = self.kwargs.get('schedule_id')
        this_schedule = Schedule.objects.get(id = schedule_id)
        form.instance.schedule = this_schedule
        form.instance.amount = this_schedule.busroute.price * form.instance.passengers
        # ... perform actions with parent_id ...
        return super().form_valid(form)
    


class ConfirmTicketView(DetailView):
    model = Ticket
    template_name = 'confirm_ticket.html'
    context_object_name = 'ticket'