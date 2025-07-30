from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shared.models import Event, Member
from shared.utils import can_register_for_event
from ..forms.create import EventCreateForm
from ..forms.update import EventUpdateForm


class EventListView(ListView):
    model = Event
    template_name = 'event_management/list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.filter(status='published').order_by('-start_datetime')


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_management/detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                member = Member.objects.get(user=self.request.user)
                can_register, message = can_register_for_event(self.object, member)
                context['can_register'] = can_register
                context['register_message'] = message
                context['is_registered'] = member in self.object.attendees.all()
            except Member.DoesNotExist:
                context['can_register'] = False
                context['register_message'] = "Member profile required"
        return context


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'event_management/create.html'
    success_url = reverse_lazy('event_management:list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Event created successfully!')
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventUpdateForm
    template_name = 'event_management/update.html'
    success_url = reverse_lazy('event_management:list')

    def form_valid(self, form):
        messages.success(self.request, 'Event updated successfully!')
        return super().form_valid(form)


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'event_management/delete.html'
    success_url = reverse_lazy('event_management:list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Event deleted successfully!')
        return super().delete(request, *args, **kwargs)


@login_required
def register_for_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    try:
        member = Member.objects.get(user=request.user)
        can_register, message = can_register_for_event(event, member)

        if can_register:
            event.attendees.add(member)
            messages.success(request, f'Successfully registered for {event.title}!')
        else:
            messages.error(request, message)
    except Member.DoesNotExist:
        messages.error(request, 'Member profile required to register for events.')

    return redirect('event_management:detail', pk=pk)