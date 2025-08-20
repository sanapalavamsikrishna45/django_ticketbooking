from django.urls import path

from .import views

urlpatterns =[
    path('', views.ScheduleList.as_view(),name ='schedule_page'),
    path('schedule/add', views.AddSchedule.as_view(), name='addschedule_page'),
    path('update/<int:pk>', views.UpdateSchedule.as_view(), name='updateschedule_page'),
    path('delete/<int:pk>', views.DeleteSchedule.as_view(), name='deleteschedule_page')
]