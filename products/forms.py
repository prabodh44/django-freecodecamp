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

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title. Title should contain CFE")
        return title



