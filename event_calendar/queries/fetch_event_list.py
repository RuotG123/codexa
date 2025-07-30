from shared.models import Event
from datetime import datetime, timedelta
from django.utils import timezone


def get_events_for_calendar(start_date=None, end_date=None):
    """Get events for calendar display within date range"""
    events = Event.objects.filter(status='published')

    if start_date:
        events = events.filter(start_datetime__date__gte=start_date)
    if end_date:
        events = events.filter(start_datetime__date__lte=end_date)

    return events.order_by('start_datetime')


def get_events_for_month(year, month):
    """Get events for a specific month"""
    start_date = datetime(year, month, 1).date()
    if month == 12:
        end_date = datetime(year + 1, 1, 1).date() - timedelta(days=1)
    else:
        end_date = datetime(year, month + 1, 1).date() - timedelta(days=1)

    return get_events_for_calendar(start_date, end_date)


def get_events_for_week(start_date):
    """Get events for a specific week"""
    end_date = start_date + timedelta(days=6)
    return get_events_for_calendar(start_date, end_date)


def get_todays_events():
    """Get events happening today"""
    today = timezone.now().date()
    return Event.objects.filter(
        start_datetime__date=today,
        status='published'
    ).order_by('start_datetime')


def get_events_in_date_range(start_date, end_date):
    """Get events within a specific date range"""
    return Event.objects.filter(
        start_datetime__date__gte=start_date,
        start_datetime__date__lte=end_date,
        status='published'
    ).order_by('start_datetime')