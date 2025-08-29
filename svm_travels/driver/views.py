from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.utils import timezone
from bus.models import Bus
from Schedule.models import Schedule

class DriverHomeView(LoginRequiredMixin, ListView):
    model = Bus
    template_name = 'driver_home.html'
    context_object_name = 'buses'

    def get_queryset(self):
        return Bus.objects.filter(driver=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()

        # Build a dictionary of today's schedules per bus
        schedules_by_bus = {}
        for bus in context['buses']:
            schedules_by_bus[bus.id] = Schedule.objects.filter(bus=bus)

        context['schedules_by_bus'] = schedules_by_bus
        return context



class DriverBusListView(ListView):
    model = Bus
    template_name = 'driver_buses.html'
    context_object_name = 'buses'

    def get_queryset(self):
        return Bus.objects.filter(driver=self.request.user)


from django.views.generic import DetailView
from Ticket.models import Ticket
from datetime import timedelta
from django.utils import timezone

class DriverBusTicketsView(DetailView):
    model = Bus
    template_name = 'driver_bus_tickets.html'
    context_object_name = 'bus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bus = self.get_object()

        # Fetch all tickets for this bus via its schedules
        tickets = Ticket.objects.filter(schedule__bus=bus).select_related('schedule', 'user')

        # Group tickets by booking_date
        grouped_tickets = {}
        for ticket in tickets:
            grouped_tickets.setdefault(ticket.booking_date, []).append(ticket)

        # Sort by date ascending
        context['grouped_tickets'] = dict(sorted(grouped_tickets.items()))

        return context
