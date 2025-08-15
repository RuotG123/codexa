from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from shared.models import Event, Speaker


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title', 'description', 'start_datetime', 'end_datetime', 'speaker'
        ]
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make speaker required
        self.fields['speaker'].required = True
        self.fields['speaker'].empty_label = "Select a speaker"

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('title', css_class='form-control'),
                Field('description', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Div(Field('start_datetime', css_class='form-control'), css_class='col-md-6'),
                Div(Field('end_datetime', css_class='form-control'), css_class='col-md-6'),
                css_class='row mb-3'
            ),
            Div(
                Field('speaker', css_class='form-control'),
                css_class='row mb-3'
            ),
            Submit('submit', 'Create Event', css_class='btn btn-primary')
        )

    def clean(self):
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get('start_datetime')
        end_datetime = cleaned_data.get('end_datetime')

        if start_datetime and end_datetime:
            if start_datetime >= end_datetime:
                raise forms.ValidationError("End time must be after start time.")

        return cleaned_data