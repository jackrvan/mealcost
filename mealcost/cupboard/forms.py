from django import forms
from .models import Item

class AddItemForm(forms.Form):
    item_name = forms.CharField(max_length=100, required=True)
    price_per_cup = forms.DecimalField(required=False)
    price_per_kg = forms.DecimalField(required=False)
    price_per_unit = forms.DecimalField(required=False)
    item_category = forms.ChoiceField(choices=Item.CATEGORY_CHOICES)

    def clean_item_name(self):
        data = self.cleaned_data["item_name"]
        return data