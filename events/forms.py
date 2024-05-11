from django import forms
from events.models import Events


class EventsModelForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
