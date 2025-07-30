from shared.models import Member
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def create_member(name, email, phone=None, membership_type='regular', user_id=None):
    """Create a new member record"""
    user = None
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            # Check if user already has a member profile
            if hasattr(user, 'member'):
                raise ValidationError("User already has a member profile")
        except User.DoesNotExist:
            pass

    member = Member.objects.create(
        name=name,
        email=email,
        phone=phone,
        membership_type=membership_type,
        user=user,
        is_active=True
    )
    return member


def update_member_details(member_id, **kwargs):
    """Update member details"""
    try:
        member = Member.objects.get(id=member_id)
        for key, value in kwargs.items():
            if hasattr(member, key):
                setattr(member, key, value)
        member.save()
        return member
    except Member.DoesNotExist:
        return None


def deactivate_member(member_id):
    """Deactivate a member"""
    try:
        member = Member.objects.get(id=member_id)
        member.is_active = False
        member.save()
        return member
    except Member.DoesNotExist:
        return None


def reactivate_member(member_id):
    """Reactivate a member"""
    try:
        member = Member.objects.get(id=member_id)
        member.is_active = True
        member.save()
        return member
    except Member.DoesNotExist:
        return None