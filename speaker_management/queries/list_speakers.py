from django.db import models
from shared.models import Speaker


def get_all_speakers():
    """Get all speakers ordered by name"""
    return Speaker.objects.all().order_by('name')


def search_speakers(query):
    """Search speakers by name, email, or expertise"""
    return Speaker.objects.filter(
        models.Q(name__icontains=query) |
        models.Q(email__icontains=query) |
        models.Q(expertise__icontains=query)
    ).order_by('name')


def get_speakers_by_expertise(expertise_keyword):
    """Get speakers with specific expertise"""
    return Speaker.objects.filter(
        expertise__icontains=expertise_keyword
    ).order_by('name')


def get_speaker_event_history(speaker_id):
    """Get event history for a specific speaker"""
    try:
        speaker = Speaker.objects.get(id=speaker_id)
        return speaker.event_set.all().order_by('-start_datetime')
    except Speaker.DoesNotExist:
        return []


def get_available_speakers():
    """Get speakers who are available (have contact info)"""
    return Speaker.objects.exclude(
        models.Q(email='') | models.Q(email__isnull=True)
    ).order_by('name')