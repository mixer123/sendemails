from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Emails
        fields = ('address',)

class EmailMassForm(forms.Form):
    text = forms.CharField(max_length=200)
    def __str__(self):
        return self.text

