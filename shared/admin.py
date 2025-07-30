from django.contrib import admin
from .models import Event, Member, Speaker


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'start_datetime', 'status', 'attendee_count']
    list_filter = ['event_type', 'status', 'start_datetime']
    search_fields = ['title', 'description']
    date_hierarchy = 'start_datetime'
    readonly_fields = ['attendee_count', 'created_at', 'updated_at']


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'membership_type', 'join_date', 'is_active']
    list_filter = ['membership_type', 'is_active', 'join_date']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'expertise']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']