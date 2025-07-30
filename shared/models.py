from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User


class Speaker(models.Model):
    """Model for managing speakers"""
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    bio = models.TextField(blank=True)
    expertise = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Member(models.Model):
    """Model for managing organization members"""
    MEMBERSHIP_TYPES = [
        ('regular', 'Regular'),
        ('premium', 'Premium'),
        ('student', 'Student'),
        ('corporate', 'Corporate'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=20, blank=True)
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPES, default='regular')
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    """Model for managing events"""
    EVENT_TYPES = [
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('webinar', 'Webinar'),
        ('meeting', 'Meeting'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=300)
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='meeting')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=500, blank=True)
    max_attendees = models.PositiveIntegerField(null=True, blank=True)
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, null=True, blank=True)
    attendees = models.ManyToManyField(Member, blank=True, related_name='events_attending')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_datetime']

    @property
    def is_upcoming(self):
        from django.utils import timezone
        return self.start_datetime > timezone.now()

    @property
    def attendee_count(self):
        return self.attendees.count()