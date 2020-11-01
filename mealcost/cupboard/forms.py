from django import forms
from .models import Item

from bootstrap_modal_forms.forms import BSModalModelForm

class AddItemForm(BSModalModelForm):
    class Meta:
        model = Item
        fields = '__all__'