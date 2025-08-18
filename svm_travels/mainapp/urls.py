from django.urls import path
from . import views

urlpatterns = [   
    path('', views.homeView, name ='homepage'),   
    path('stops/', views.StopList.as_view(), name = 'stops_page'),
    path('stops/add', views.AddStop.as_view(), name='addstop_page'),
    path('stops/update/<int:pk>', views.UpdateProduct.as_view(), name = 'update_stop'),
    path('stops/delete/<int:pk>', views.DeleteStop.as_view(), name = 'delete_stop')
    
]