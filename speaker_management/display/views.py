from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shared.models import Speaker
from ..forms.create import SpeakerCreateForm
from ..forms.update import SpeakerUpdateForm


class SpeakerListView(ListView):
    model = Speaker
    template_name = 'speaker_management/list.html'
    context_object_name = 'speakers'
    paginate_by = 20

    def get_queryset(self):
        return Speaker.objects.all().order_by('name')


class SpeakerDetailView(DetailView):
    model = Speaker
    template_name = 'speaker_management/detail.html'
    context_object_name = 'speaker'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_events'] = self.object.event_set.all()[:5]
        return context


class SpeakerCreateView(LoginRequiredMixin, CreateView):
    model = Speaker
    form_class = SpeakerCreateForm
    template_name = 'speaker_management/create.html'
    success_url = reverse_lazy('speaker_management:list')

    def form_valid(self, form):
        messages.success(self.request, 'Speaker created successfully!')
        return super().form_valid(form)


class SpeakerUpdateView(LoginRequiredMixin, UpdateView):
    model = Speaker
    form_class = SpeakerUpdateForm
    template_name = 'speaker_management/update.html'
    success_url = reverse_lazy('speaker_management:list')

    def form_valid(self, form):
        messages.success(self.request, 'Speaker updated successfully!')
        return super().form_valid(form)


class SpeakerDeleteView(LoginRequiredMixin, DeleteView):
    model = Speaker
    template_name = 'speaker_management/delete.html'
    success_url = reverse_lazy('speaker_management:list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Speaker deleted successfully!')
        return super().delete(request, *args, **kwargs)