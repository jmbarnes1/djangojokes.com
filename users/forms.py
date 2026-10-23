from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

BIRTH_YEAR_CHOICES = range(1915, datetime.now().year)

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class CustomUserChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'dob')
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years = BIRTH_YEAR_CHOICES
            )
        }

"""
Things to notice:

You inherit from UserChangeForm to create your CustomUserChangeForm class. Note that 
    UserChangeForm is imported toward the top of the file.
You set password to None, because passwords are stored in an encrypted format. That’s 
    why you created a separate change-password form.
In the Meta inner class:
You use get_user_model() as the model. Note that get_user_model is imported toward 
    the top of the file.
You set the fields that you want in the form.
You specify that you want to use SelectDateWidget for the dob field. Note that 
    before the class definition, BIRTH_YEAR_CHOICES is set to hold a range of years. 
    You assign BIRTH_YEAR_CHOICES to years in the SelectDateWidget.
"""