from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User


class Speaker(models.Model):
    """Model for managing speakers"""
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    bio = models.TextField(blank=True)
    company_name = models.CharField(max_length=200, blank=True, help_text="Speaker's company or organization")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Member(models.Model):
    """Model for managing organization members"""
    MEMBERSHIP_ROLES = [
        ('student', 'Student'),
        ('admin', 'Admin/Staff'),
    ]

    # Year choices for students
    YEAR_CHOICES = [
        ('freshman', 'Freshman'),
        ('sophomore', 'Sophomore'),
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('graduate', 'Graduate'),
        ('alumni', 'Alumni'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    membership_role = models.CharField(max_length=20, choices=MEMBERSHIP_ROLES, default='student')

    # Academic information
    major = models.CharField(max_length=100, blank=True, help_text="Student's major/field of study")
    year = models.CharField(max_length=20, choices=YEAR_CHOICES, blank=True, help_text="Academic year level")

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    """Model for managing events - simplified to match ERD"""
    title = models.CharField(max_length=300)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)  # Now required
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