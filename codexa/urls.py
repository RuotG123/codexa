"""
URL configuration for codexa project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/events/', permanent=False)),
    path('events/', include('event_management.urls')),
    path('members/', include('member_management.urls')),
    path('speakers/', include('speaker_management.urls')),
    path('calendar/', include('event_calendar.urls')),
]