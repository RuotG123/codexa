"""
URL configuration for codexa project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_system.urls')),
    path('events/', include('event_management.urls')),
    path('members/', include('member_management.urls')),
    path('speakers/', include('speaker_management.urls')),
    path('calendar/', include('event_calendar.urls')),
]