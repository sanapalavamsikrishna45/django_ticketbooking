from django.urls import path
from .import views
urlpatterns = [
   path('', views.RouteList.as_view(), name='route_page'),
   path('route/add', views.AddRoute.as_view(), name='addroute_page'),
   path('update/<int:pk>', views.UpdateRoute.as_view(), name='updateroute_page'),
   path('delete/<int:pk>', views.DeleteRoute.as_view(), name='deleteroute_page')
]