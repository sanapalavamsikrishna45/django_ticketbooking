from django.urls import path
from . import views

urlpatterns = [   
    path('', views.homeView, name ='homepage'),   
    path('stops', views.StopList.as_view(), name = 'stops_page')
    
]