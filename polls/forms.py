from django import forms
from.models import rsvp

class rsvp_form(forms.ModelForm):
    class Meta:
        model = rsvp
        fields = [
            'name',
            'guest',
            'email',
            "attend",
            'message'
        ]
