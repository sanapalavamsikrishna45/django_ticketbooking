from django.urls import path
from .import views
urlpatterns =[
    # path('buss/', views.busView, name='bus_page'),
    path('', views.BusList.as_view(), name='bus_page'),
    path('add', views.AddBus.as_view(), name='addbus_page'),
    path('update/<int:pk>', views.UpdateBus.as_view(), name='updatebus_page'),
    path('delete/<int:pk>', views.DeleteBus.as_view(), name = 'deletebus_page')
]