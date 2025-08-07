from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from shared.models import Event, Member
from shared.utils import can_register_for_event
from ..forms.create import EventCreateForm
from ..forms.update import EventUpdateForm


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'event_management/list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.filter(status='published').order_by('-start_datetime')


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'event_management/detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # For admin-only system, no registration logic needed
        context['can_register'] = False
        context['is_registered'] = False
        context['register_message'] = "Contact admin to register for events"
        return context


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'event_management/create.html'
    success_url = reverse_lazy('event_management:list')

    def form_valid(self, form):
        messages.success(self.request, 'Event updated successfully!')
        return super().form_valid(form)

# DeleteView removed - not in structure chartvalid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Event created successfully!')
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventUpdateForm
    template_name = 'event_management/update.html'
    success_url = reverse_lazy('event_management:list')

    def form_