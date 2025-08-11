# event_management/forms/update.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from shared.models import Event


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'event_type', 'status',
            'start_datetime', 'end_datetime', 'location',
            'max_attendees', 'speaker'
        ]
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Field('title', css_class='form-control'),
                Field('description', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Div(Field('event_type', css_class='form-control'), css_class='col-md-6'),
                Div(Field('status', css_class='form-control'), css_class='col-md-6'),
                css_class='row mb-3'
            ),
            Div(
                Div(Field('start_datetime', css_class='form-control'), css_class='col-md-6'),
                Div(Field('end_datetime', css_class='form-control'), css_class='col-md-6'),
                css_class='row mb-3'
            ),
            Div(
                Field('location', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Div(Field('max_attendees', css_class='form-control'), css_class='col-md-6'),
                Div(Field('speaker', css_class='form-control'), css_class='col-md-6'),
                css_class='row mb-3'
            ),
            Submit('submit', 'Update Event', css_class='btn btn-primary')
        )

    def clean(self):
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get('start_datetime')
        end_datetime = cleaned_data.get('end_datetime')

        if start_datetime and end_datetime:
            if start_datetime >= end_datetime:
                raise forms.ValidationError("End time must be after start time.")

        return cleaned_data