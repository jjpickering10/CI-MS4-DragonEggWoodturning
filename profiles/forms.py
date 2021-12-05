from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for user profile
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)
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

    def __init__(self, *args, **kwargs):
        """
        Set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs['autofocus'] = True
