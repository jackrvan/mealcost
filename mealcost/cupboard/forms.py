from django import forms

class AddItemForm(forms.Form):
    item_name = forms.CharField(max_length=100)
    price_per_cup = forms.DecimalField(max_digits=7, decimal_places=2)
    price_per_kg = forms.DecimalField(max_digits=7, decimal_places=2)
    price_per_unit = forms.DecimalField(max_digits=7, decimal_places=2)
