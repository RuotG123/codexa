# Generated migration for model field cleanup
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('shared', '0004_remove_speaker_phone_member_major_member_year'),
    ]

    operations = [
        # Remove fields from Event model that aren't in ERD
        migrations.RemoveField(
            model_name='event',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.RemoveField(
            model_name='event',
            name='max_attendees',
        ),

        # Remove fields from Member model that aren't in ERD
        migrations.RemoveField(
            model_name='member',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='join_date',
        ),

        # Remove expertise from Speaker and add company_name
        migrations.RemoveField(
            model_name='speaker',
            name='expertise',
        ),
        migrations.AddField(
            model_name='speaker',
            name='company_name',
            field=models.CharField(blank=True, help_text="Speaker's company or organization", max_length=200),
        ),

        # Rename membership_type to membership_role in Member
        migrations.RenameField(
            model_name='member',
            old_name='membership_type',
            new_name='membership_role',
        ),

        # Make speaker field required in Event (remove null=True, blank=True)
        migrations.AlterField(
            model_name='event',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared.speaker'),
        ),
    ]