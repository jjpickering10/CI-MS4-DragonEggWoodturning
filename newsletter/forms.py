from django import forms
from .models import Subscribers, Newsletter


class SubscribersForm(forms.ModelForm):
    """
    Form for subscribers
    """
    class Meta:
        model = Subscribers
        fields = ['email']


class NewsletterForm(forms.ModelForm):
    """
    Form for newsletter
    """
    class Meta:
        model = Newsletter
        fields = ['title', 'message']
