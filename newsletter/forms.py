from django import forms
from .models import Subscribers, Newsletter


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'message']
