from django.urls import path

from .import views
from . import api_views

urlpatterns =[
    path('', views.ScheduleList.as_view(),name ='schedule_page'),
    path('search/', views.search_schedule, name='search_schedule'),
    path('schedule/add', views.AddSchedule.as_view(), name='addschedule_page'),
    path('update/<int:pk>', views.UpdateSchedule.as_view(), name='updateschedule_page'),
    path('delete/<int:pk>', views.DeleteSchedule.as_view(), name='deleteschedule_page'),
    path('api/search-schedules/', api_views.schedule_search_api, name='schedule-search-api'),
]