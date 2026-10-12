from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )

JOBS = (
    (None,' -- '),
    ('Full-time','Full-time'),
    ('Part-time','Part-time'),
    ('Contract','Contract')
)

WORKDAYS = (
    ('MON','MON'),
    ('TUE','TUE'),
    ('WED','WED'),
    ('THU','THU'),
    ('FRI','FRI'),
)

"""
forms.ChoiceField
forms.MultipleChoiceField
forms.NullBooleanField
forms.TypedChoiceField
forms.TypedMultipleChoiceField
"""

class JobApplicationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus' : True
            }
        )
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.CharField(
        required=False,
        widget=forms.URLInput(
            attrs={
            'size':'50',
            'class':'form-control',
            'placeholder':'https://www.example.com',
            }
        ),
        validators=[URLValidator(schemes=['http', 'https'])]
    )
    employment_type = forms.ChoiceField(choices=JOBS)
    start_date = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            years=range(2026, 2027),
            empty_label=("Choose Year","Choose Month","Choose Day"),
            attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'}
        ),
        validators=[validate_future_date],
        error_messages = {'past_date': 'Please enter a future date.'}
    )
    available_days = forms.MultipleChoiceField(
        choices=WORKDAYS,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'checked':True
            }
        )
    )
    desired_hourly_wage  = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'min':'10:00',
                'max':'100.00',
                'step':'.25'
            }
        )
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols':'75','rows':'5'}
        )
    )
    # cover_letter = forms.FileField()
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true',
        required=True)