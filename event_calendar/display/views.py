from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
from shared.models import Event
from shared.utils import get_events_by_date_range


class CalendarView(TemplateView):
    """Public view - no login required"""
    template_name = 'calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(
            start_datetime__gte=timezone.now(),
            status='published'
        )[:5]
        return context


class EventAPIView(View):
    """Public API - no login required"""
    def get(self, request):
        """Return events in JSON format for calendar display"""
        start_date = request.GET.get('start')
        end_date = request.GET.get('end')

        if start_date and end_date:
            try:
                start = datetime.fromisoformat(start_date.replace('Z', '+00:00')).date()
                end = datetime.fromisoformat(end_date.replace('Z', '+00:00')).date()
                events = get_events_by_date_range(start, end)
            except ValueError:
                events = Event.objects.filter(status='published')
        else:
            events = Event.objects.filter(status='published')

        event_list = []
        for event in events:
            event_list.append({
                'id': event.id,
                'title': event.title,
                'start': event.start_datetime.isoformat(),
                'end': event.end_datetime.isoformat(),
                'url': f'/events/{event.id}/',
                'backgroundColor': self.get_event_color(event.event_type),
                'borderColor': self.get_event_color(event.event_type),
                'description': event.description[:100] + '...' if len(event.description) > 100 else event.description,
                'location': event.location or 'TBD',
            })

        return JsonResponse(event_list, safe=False)

    def get_event_color(self, event_type):
        """Return color based on event type"""
        colors = {
            'conference': '#007bff',
            'workshop': '#28a745',
            'seminar': '#ffc107',
            'webinar': '#17a2b8',
            'meeting': '#6c757d',
        }
        return colors.get(event_type, '#6c757d')