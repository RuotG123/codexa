from django.utils import timezone
from django.db.models import Q
from datetime import datetime, timedelta


def get_upcoming_events():
    """Get events that are scheduled for the future"""
    from shared.models import Event
    return Event.objects.filter(
        start_datetime__gte=timezone.now()
    ).order_by('start_datetime')


def get_past_events():
    """Get events that have already occurred"""
    from shared.models import Event
    return Event.objects.filter(
        end_datetime__lt=timezone.now()
    ).order_by('-start_datetime')


def get_events_by_date_range(start_date, end_date):
    """Get events within a specific date range"""
    from shared.models import Event
    return Event.objects.filter(
        start_datetime__date__gte=start_date,
        start_datetime__date__lte=end_date
    ).order_by('start_datetime')


def format_event_datetime(event):
    """Format event datetime for display"""
    start = event.start_datetime.strftime('%Y-%m-%d %H:%M')
    end = event.end_datetime.strftime('%Y-%m-%d %H:%M')
    return f"{start} - {end}"