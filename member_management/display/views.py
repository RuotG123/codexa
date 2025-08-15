from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from shared.models import Member
from ..forms.create import MemberCreateForm
from ..forms.update import MemberUpdateForm


class MemberListView(ListView):
    """Public view - no login required"""
    model = Member
    template_name = 'member_management/list.html'
    context_object_name = 'members'
    paginate_by = 20

    def get_queryset(self):
        return Member.objects.filter(is_active=True).order_by('name')


class MemberDetailView(DetailView):
    """Public view - no login required"""
    model = Member
    template_name = 'member_management/detail.html'
    context_object_name = 'member'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Since we removed attendees field, we don't show recent events
        return context


class MemberCreateView(LoginRequiredMixin, CreateView):
    """Admin only - login required"""
    model = Member
    form_class = MemberCreateForm
    template_name = 'member_management/create.html'
    success_url = reverse_lazy('member_management:list')

    def form_valid(self, form):
        messages.success(self.request, 'Member created successfully!')
        return super().form_valid(form)


class MemberUpdateView(LoginRequiredMixin, UpdateView):
    """Admin only - login required"""
    model = Member
    form_class = MemberUpdateForm
    template_name = 'member_management/update.html'
    success_url = reverse_lazy('member_management:list')

    def form_valid(self, form):
        messages.success(self.request, 'Member updated successfully!')
        return super().form_valid(form)


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    """Admin only - login required"""
    model = Member
    template_name = 'member_management/delete.html'
    success_url = reverse_lazy('member_management:list')
    context_object_name = 'member'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Member deleted successfully!')
        return super().delete(request, *args, **kwargs)