from django.urls import path
from .import views
urlpatterns =[
    # path('')
    path('', views.BookTicketView.as_view(), name='ticket_page')
   
]