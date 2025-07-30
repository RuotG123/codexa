from shared.models import Event, Speaker
from django.contrib.auth.models import User
from django.utils import timezone


def create_event(title, description, event_type, start_datetime, end_datetime,
                 created_by, location=None, max_attendees=None, speaker_id=None):
    """Create a new event record"""
    speaker = None
    if speaker_id:
        try:
            speaker = Speaker.objects.get(id=speaker_id)
        except Speaker.DoesNotExist:
            pass

    event = Event.objects.create(
        title=title,
        description=description,
        event_type=event_type,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        location=location,
        max_attendees=max_attendees,
        speaker=speaker,
        created_by=created_by,
        status='draft'
    )
    return event


def publish_event(event_id):
    """Change event status to published"""
    try:
        event = Event.objects.get(id=event_id)
        event.status = 'published'
        event.save()
        return event
    except Event.DoesNotExist:
        return None


def cancel_event(event_id):
    """Cancel an event"""
    try:
        event = Event.objects.get(id=event_id)
        event.status = 'cancelled'
        event.save()
        return event
    except Event.DoesNotExist:
        return None


def update_event_details(event_id, **kwargs):
    """Update event details"""
    try:
        event = Event.objects.get(id=event_id)
        for key, value in kwargs.items():
            if hasattr(event, key):
                setattr(event, key, value)
        event.save()
        return event
    except Event.DoesNotExist:
        return None