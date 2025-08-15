from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from shared.models import Member


class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'membership_role', 'major', 'year', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add helpful labels and help text
        self.fields['major'].label = 'Major/Field of Study'
        self.fields['year'].label = 'Academic Year'
        self.fields['membership_role'].label = 'Membership Role'
        self.fields['major'].help_text = 'Enter the student\'s major or field of study'
        self.fields['year'].help_text = 'Select the current academic year level'

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('name', css_class='form-control'),
                Field('email', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Field('membership_role', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Div(Field('major', css_class='form-control'), css_class='col-md-6'),
                Div(Field('year', css_class='form-control'), css_class='col-md-6'),
                css_class='row mb-3'
            ),
            Div(
                Field('is_active', css_class='form-check-input'),
                css_class='row mb-3'
            ),
            Submit('submit', 'Update Member', css_class='btn btn-primary')
        )