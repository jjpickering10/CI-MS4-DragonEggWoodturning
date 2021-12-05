from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for order
    """
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'county',
            'postcode',
            'country',
        )
