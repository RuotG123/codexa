from django.urls import path
from .display import views

app_name = 'calendar'

urlpatterns = [
    path('', views.CalendarView.as_view(), name='view'),
    path('api/events/', views.EventAPIView.as_view(), name='api_events'),
]