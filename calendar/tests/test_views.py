import pytest
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from shared.models import Event, Speaker
from datetime import datetime, timedelta
from django.utils import timezone


class EventViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.speaker = Speaker.objects.create(
            name='Test Speaker',
            email='speaker@example.com'
        )

    def test_event_list_view(self):
        """Test that event list view displays events"""
        # Create a published event
        Event.objects.create(
            title='Test Event',
            description='Test Description',
            event_type='conference',
            status='published',
            start_datetime=timezone.now() + timedelta(days=1),
            end_datetime=timezone.now() + timedelta(days=1, hours=2),
            created_by=self.user
        )

        response = self.client.get(reverse('event_management:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_detail_view(self):
        """Test event detail view"""
        event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            event_type='conference',
            status='published',
            start_datetime=timezone.now() + timedelta(days=1),
            end_datetime=timezone.now() + timedelta(days=1, hours=2),
            created_by=self.user
        )

        response = self.client.get(reverse('event_management:detail', kwargs={'pk': event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_event_create_requires_login(self):
        """Test that creating events requires login"""
        response = self.client.get(reverse('event_management:create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_event_create_with_login(self):
        """Test creating event when logged in"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('event_management:create'))
        self.assertEqual(response.status_code, 200)