# event_management/display/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from shared.models import Event, Speaker
from ..forms.create import EventCreateForm
from ..forms.update import EventUpdateForm


class EventListView(ListView):
    """Display a list of all events."""
    model = Event
    template_name = 'event_management/list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        """Return all events ordered by start date."""
        return Event.objects.all().order_by('start_datetime')


class EventDetailView(DetailView):
    """Display details for a single event."""
    model = Event
    template_name = 'event_management/detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        """Return all events (no status filtering since status field removed)."""
        return Event.objects.all()


class EventCreateView(LoginRequiredMixin, CreateView):
    """Create a new event."""
    model = Event
    form_class = EventCreateForm
    template_name = 'event_management/create.html'

    def form_valid(self, form):
        """Set the created_by field and add success message."""
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Event created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to event detail page after creation."""
        return reverse_lazy('event_management:detail', kwargs={'pk': self.object.pk})


class EventUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing event."""
    model = Event
    form_class = EventUpdateForm
    template_name = 'event_management/update.html'
    context_object_name = 'event'

    def form_valid(self, form):
        """Add success message when event is updated."""
        messages.success(self.request, 'Event updated successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to event detail page after update."""
        return reverse_lazy('event_management:detail', kwargs={'pk': self.object.pk})