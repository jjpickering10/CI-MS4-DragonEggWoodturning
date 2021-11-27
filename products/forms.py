from django import forms
from .models import Review, Product, Category, WoodType, Image


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'body',
            'rating',
        )

    # def __init__(self, *args, **kwargs):
    #     """
    #     Set autofocus on first field
    #     """
    #     super().__init__(*args, **kwargs)

    #     self.fields['body'].widget.attrs['autofocus'] = True


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['discount_choices']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['multiple'] = True


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'wood_type', 'name', 'description', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        wood_types = WoodType.objects.all()
        cat_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        wood_friendly_names = [(w.id, w.get_friendly_name()) for w in wood_types]

        self.fields['category'].choices = cat_friendly_names
        self.fields['wood_type'].choices = wood_friendly_names
        self.fields['price'].widget.attrs['min'] = 0
