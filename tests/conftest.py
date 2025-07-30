import pytest
from django.test import Client
from django.contrib.auth.models import User
from shared.models import Event, Member, Speaker
from datetime import datetime, timedelta
from django.utils import timezone


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user():
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )


@pytest.fixture
def admin_user():
    return User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpass123'
    )


@pytest.fixture
def speaker():
    return Speaker.objects.create(
        name='John Doe',
        email='john@example.com',
        bio='Expert in technology',
        expertise='Django, Python, Web Development',
        phone='+1234567890'
    )


@pytest.fixture
def member(user):
    return Member.objects.create(
        user=user,
        name='Jane Smith',
        email='jane@example.com',
        phone='+0987654321',
        membership_type='regular'
    )


@pytest.fixture
def event(user, speaker):
    return Event.objects.create(
        title='Test Event',
        description='This is a test event',
        event_type='conference',
        status='published',
        start_datetime=timezone.now() + timedelta(days=7),
        end_datetime=timezone.now() + timedelta(days=7, hours=2),
        location='Test Venue',
        max_attendees=100,
        speaker=speaker,
        created_by=user
    )