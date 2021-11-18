from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'body',
            'rating',
        )

    def __init__(self, *args, **kwargs):
        """
        Set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['body'].widget.attrs['autofocus'] = True
