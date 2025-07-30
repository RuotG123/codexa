from django.urls import path
from .views import CalendarView, EventAPIView

urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
    path('api/events/', EventAPIView.as_view(), name='api_events'),
]