from rest_framework import serializers
from .models import Event, Member, Speaker


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ['id', 'name', 'email', 'bio', 'expertise', 'phone']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'phone', 'membership_type', 'join_date', 'is_active']


class EventSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer(read_only=True)
    attendees = MemberSerializer(many=True, read_only=True)
    attendee_count = serializers.ReadOnlyField()
    is_upcoming = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'event_type', 'status',
            'start_datetime', 'end_datetime', 'location', 'max_attendees',
            'speaker', 'attendees', 'attendee_count', 'is_upcoming',
            'created_at', 'updated_at'
        ]