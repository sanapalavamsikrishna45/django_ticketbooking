from django.urls import path
from .views import DriverHomeView, DriverBusListView, DriverBusTicketsView

urlpatterns = [
    path('driver/home/', DriverHomeView.as_view(), name='driver_home'),
    path('driver/buses/', DriverBusListView.as_view(), name='driver_buses'),
    path('driver/buses/<int:pk>/tickets/', DriverBusTicketsView.as_view(), name='driver_bus_tickets'),
]
