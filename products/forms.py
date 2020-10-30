from django import forms

from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title',
                  'description',
                  'price']


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs = {
        'class': 'new-class class-for-description',
        # a CSS class
        'rows': 30,
        'cols': 60,
        'placeholder': " .new-class .class-for-description rows = 30 cols = 60"
    }))
    price = forms.DecimalField()


