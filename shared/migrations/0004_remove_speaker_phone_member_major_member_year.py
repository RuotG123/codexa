# Generated migration for model updates
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_alter_member_membership_type'),
    ]

    operations = [
        # Add new fields to Member model
        migrations.AddField(
            model_name='member',
            name='major',
            field=models.CharField(blank=True, help_text="Student's major/field of study", max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='year',
            field=models.CharField(blank=True, choices=[('freshman', 'Freshman'), ('sophomore', 'Sophomore'), ('junior', 'Junior'), ('senior', 'Senior'), ('graduate', 'Graduate'), ('alumni', 'Alumni')], help_text='Academic year level', max_length=20),
        ),
        # Remove phone field from Speaker model
        migrations.RemoveField(
            model_name='speaker',
            name='phone',
        ),
    ]