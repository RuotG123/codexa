from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from shared.models import Speaker


class SpeakerCreateForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ['name', 'email', 'phone', 'bio', 'expertise']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'expertise': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('name', css_class='form-control'),
                Field('email', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Field('phone', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Field('expertise', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Field('bio', css_class='form-control'),
                css_class='row mb-3'
            ),
            Submit('submit', 'Create Speaker', css_class='btn btn-primary')
        )