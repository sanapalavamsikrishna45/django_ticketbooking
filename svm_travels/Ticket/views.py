from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
from django.urls import reverse_lazy
from .models import Ticket


class BookTicketView(CreateView):
    model = Ticket
    template_name = 'book_ticket.html'
    # context_object_name = 'ticket'
    fields = '__all__'
    success_url = reverse_lazy('')
