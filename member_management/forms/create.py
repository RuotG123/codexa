from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field
from shared.models import Member
from django.contrib.auth.models import User


class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'membership_type', 'user']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(member__isnull=True)
        self.fields['user'].required = False

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('name', css_class='form-control'),
                Field('email', css_class='form-control'),
                css_class='row mb-3'
            ),
            Div(
                Div(Field('phone', css_class='form-control'), css_class='col-md-6'),
                Div(Field('membership_type', css_class='form-control'), css_class='col-md-6'),
                css_class='row mb-3'
            ),
            Div(
                Field('user', css_class='form-control'),
                css_class='row mb-3'
            ),
            Submit('submit', 'Create Member', css_class='btn btn-primary')
        )