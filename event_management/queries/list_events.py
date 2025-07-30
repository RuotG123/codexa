from django.db import models
from shared.models import Event
from django.utils import timezone


def get_published_events():
    """Get all published events ordered by start date"""
    return Event.objects.filter(status='published').order_by('start_datetime')


def get_upcoming_events():
    """Get upcoming published events"""
    return Event.objects.filter(
        status='published',
        start_datetime__gte=timezone.now()
    ).order_by('start_datetime')


def get_past_events():
    """Get past events"""
    return Event.objects.filter(
        end_datetime__lt=timezone.now()
    ).order_by('-start_datetime')


def get_events_by_type(event_type):
    """Get events filtered by type"""
    return Event.objects.filter(
        event_type=event_type,
        status='published'
    ).order_by('start_datetime')


def get_events_by_speaker(speaker):
    """Get events by specific speaker"""
    return Event.objects.filter(
        speaker=speaker,
        status='published'
    ).order_by('start_datetime')


def search_events(query):
    """Search events by title or description"""
    return Event.objects.filter(
        models.Q(title__icontains=query) | models.Q(description__icontains=query),
        status='published'
    ).order_by('start_datetime')