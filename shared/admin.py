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
    list_display = ['name', 'email', 'membership_type', 'major', 'year', 'join_date', 'is_active']
    list_filter = ['membership_type', 'year', 'is_active', 'join_date']
    search_fields = ['name', 'email', 'major']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'user')
        }),
        ('Membership Information', {
            'fields': ('membership_type', 'is_active')
        }),
        ('Academic Information', {
            'fields': ('major', 'year'),
            'description': 'Academic details for student members'
        }),
        ('System Information', {
            'fields': ('join_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'expertise']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Professional Information', {
            'fields': ('expertise', 'bio')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )