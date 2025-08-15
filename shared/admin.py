# shared/admin.py
from django.contrib import admin
from .models import Event, Member, Speaker


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_datetime', 'speaker', 'attendee_count']
    list_filter = ['start_datetime', 'speaker']
    search_fields = ['title', 'description', 'speaker__name']
    date_hierarchy = 'start_datetime'
    readonly_fields = ['attendee_count', 'created_at', 'updated_at']

    fieldsets = (
        ('Event Information', {
            'fields': ('title', 'description', 'speaker')
        }),
        ('Schedule', {
            'fields': ('start_datetime', 'end_datetime')
        }),
        ('Registration', {
            'fields': ('attendees', 'attendee_count'),
            'description': 'Manage event attendees'
        }),
        ('System Information', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    filter_horizontal = ('attendees',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'membership_role', 'major', 'year', 'is_active']
    list_filter = ['membership_role', 'year', 'is_active']
    search_fields = ['name', 'email', 'major']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'user')
        }),
        ('Membership Information', {
            'fields': ('membership_role', 'is_active')
        }),
        ('Academic Information', {
            'fields': ('major', 'year'),
            'description': 'Academic details for student members'
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'company_name', 'created_at']
    search_fields = ['name', 'email', 'company_name', 'bio']
    list_filter = ['created_at', 'company_name']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Professional Information', {
            'fields': ('company_name', 'bio')
        }),
        ('System Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )