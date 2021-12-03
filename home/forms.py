from django import forms


class ContactForm(forms.Form):
    """
    Contact form for contact page
    """
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
