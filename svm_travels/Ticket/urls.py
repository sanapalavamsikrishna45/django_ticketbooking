from django.urls import path
from .import views

from . import api_views
urlpatterns =[
    # path('')
    path('book/<int:schedule_id>', views.BookTicketView.as_view(), name='book_ticket'),
    path('confirm/<int:pk>/', views.ConfirmTicketView.as_view(), name='confirm_ticket'),
    path('api/passengers/', api_views.PassengerListAPI.as_view(), name='passenger-list-api'),
    path('api/passengers/add/', api_views.PassengerAddAPI.as_view(), name='passenger-add-api'),
    path('my-tickets/', views.MyTicketsView.as_view(), name='my_tickets'),
   
]