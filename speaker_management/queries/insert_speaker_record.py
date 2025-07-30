from shared.models import Speaker
from django.core.exceptions import ValidationError


def create_speaker(name, email, bio=None, expertise=None, phone=None):
    """Create a new speaker record"""
    # Check for duplicate email
    if Speaker.objects.filter(email=email).exists():
        raise ValidationError("Speaker with this email already exists")

    speaker = Speaker.objects.create(
        name=name,
        email=email,
        bio=bio or '',
        expertise=expertise or '',
        phone=phone or ''
    )
    return speaker


def update_speaker_details(speaker_id, **kwargs):
    """Update speaker details"""
    try:
        speaker = Speaker.objects.get(id=speaker_id)
        for key, value in kwargs.items():
            if hasattr(speaker, key):
                setattr(speaker, key, value)
        speaker.save()
        return speaker
    except Speaker.DoesNotExist:
        return None


def delete_speaker(speaker_id):
    """Delete a speaker if they have no associated events"""
    try:
        speaker = Speaker.objects.get(id=speaker_id)
        if speaker.event_set.exists():
            raise ValidationError("Cannot delete speaker with associated events")
        speaker.delete()
        return True
    except Speaker.DoesNotExist:
        return False