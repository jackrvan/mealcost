from django import forms
from .models import Item

from bootstrap_modal_forms.forms import BSModalForm

class AddItemForm(BSModalForm):
    class Meta:
        model = Item
        fields = '__all__'
