from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from shared.models import Speaker


class SpeakerCreateForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ['name', 'email', 'company_name', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company_name'].label = 'Company/Organization'
        self.fields['company_name'].help_text = 'Speaker\'s company or organization'

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('name', css_class='form-control'),
                Field('email', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Field('company_name', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Field('bio', css_class='form-control'),
                css_class='row mb-3'
            ),
            Submit('submit', 'Create Speaker', css_class='btn btn-primary')
        )