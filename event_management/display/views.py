from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shared.models import Event, Speaker


class EventListView(ListView):
    """Display a list of all events."""
    model = Event
    template_name = 'event_management/list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        """Return published events ordered by start date."""
        return Event.objects.filter(status='published').order_by('start_datetime')


class EventDetailView(DetailView):
    """Display details for a single event."""
    model = Event
    template_name = 'event_management/detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        """Allow staff to see all events, others only published ones."""
        if self.request.user.is_staff:
            return Event.objects.all()
        return Event.objects.filter(status='published')


class EventCreateView(LoginRequiredMixin, CreateView):
    """Create a new event."""
    model = Event
    template_name = 'event_management/create.html'
    fields = [
        'title', 'description', 'event_type', 'start_datetime',
        'end_datetime', 'location', 'speaker', 'max_attendees', 'status'
    ]

    def form_valid(self, form):
        """Add success message when event is created."""
        messages.success(self.request, 'Event created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to event detail page after creation."""
        return reverse_lazy('event_management:detail', kwargs={'pk': self.object.pk})


class EventUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing event."""
    model = Event
    template_name = 'event_management/update.html'
    fields = [
        'title', 'description', 'event_type', 'start_datetime',
        'end_datetime', 'location', 'speaker', 'max_attendees', 'status'
    ]
    context_object_name = 'event'

    def form_valid(self, form):
        """Add success message when event is updated."""
        messages.success(self.request, 'Event updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to event detail page after update."""
        return reverse_lazy('event_management:detail', kwargs={'pk': self.object.pk})


class EventDeleteView(LoginRequiredMixin, DeleteView):
    """Delete an existing event."""
    model = Event
    template_name = 'event_management/delete.html'
    context_object_name = 'event'
    success_url = reverse_lazy('event_management:list')

    def delete(self, request, *args, **kwargs):
        """Add success message when event is deleted."""
        messages.success(self.request, 'Event deleted successfully!')
        return super().delete(request, *args, **kwargs)