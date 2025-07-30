from django.db import models
from shared.models import Member


def get_active_members():
    """Get all active members"""
    return Member.objects.filter(is_active=True).order_by('name')


def get_all_members():
    """Get all members regardless of status"""
    return Member.objects.all().order_by('name')


def get_members_by_type(membership_type):
    """Get members by membership type"""
    return Member.objects.filter(
        membership_type=membership_type,
        is_active=True
    ).order_by('name')


def search_members(query):
    """Search members by name or email"""
    return Member.objects.filter(
        models.Q(name__icontains=query) | models.Q(email__icontains=query),
        is_active=True
    ).order_by('name')


def get_recent_members(days=30):
    """Get members who joined in the last N days"""
    from django.utils import timezone
    from datetime import timedelta

    cutoff_date = timezone.now().date() - timedelta(days=days)
    return Member.objects.filter(
        join_date__gte=cutoff_date,
        is_active=True
    ).order_by('-join_date')


def get_member_event_history(member_id):
    """Get event history for a specific member"""
    try:
        member = Member.objects.get(id=member_id)
        return member.events_attending.all().order_by('-start_datetime')
    except Member.DoesNotExist:
        return []