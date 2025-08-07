"""
URL configuration for codexa project.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_events(request):
    """Redirect root URL to events list for public access"""
    return redirect('event_management:list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_events),
    path('login/', include('login_system.urls')),
    path('events/', include('event_management.urls')),
    path('members/', include('member_management.urls')),
    path('speakers/', include('speaker_management.urls')),
    path('calendar/', include('event_calendar.urls')),
]