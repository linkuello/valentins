from django import forms
from .models import ValentineCard

class ValentineCardForm(forms.ModelForm):
    class Meta:
        model = ValentineCard
        fields = ['sender_name', 'recipient_email', 'message']

