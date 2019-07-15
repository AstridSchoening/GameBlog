from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
         model = Event
         fields = ('zeitpunkt', 'title',  'author','text','twitchlink')
         widgets = { 'zeitpunkt': forms.DateTimeInput(attrs={'class': 'datetime-input'}) }