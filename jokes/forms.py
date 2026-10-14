from django.forms import ModelForm, Textarea, CheckboxSelectMultiple

from .models import Joke

class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['question', 'answer','category','tags']
        widgets = {
            'question': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            ),
            'answer': Textarea(
                attrs={'cols': 80, 'rows': 2, 'placeholder': 'Make it funny!'}
            ),
            'tags': CheckboxSelectMultiple()
        }
        help_texts = {
            'question': 'No dirty jokes please.'
        }

"""
available_days = forms.MultipleChoiceField(
    choices=WORKDAYS,
    widget=forms.CheckboxSelectMultiple(
        attrs={
            'checked':True
        }
    )
)
"""