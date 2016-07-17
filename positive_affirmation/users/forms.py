from django import forms

from .models import Affirmation


class CreateAffirmationForm(forms.ModelForm):
    class Meta:
        model = Affirmation
        fields = ('text',)
