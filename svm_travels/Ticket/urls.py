from django.urls import path
from .import views
urlpatterns =[
    # path('')
    path('book/<int:schedule_id>', views.BookTicketView.as_view(), name='book_ticket'),
    path('confirm/<int:pk>/', views.ConfirmTicketView.as_view(), name='confirm_ticket'),
   
]