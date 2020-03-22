from .models import Item
from bootstrap_modal_forms.forms import BSModalForm

class AddItemForm(BSModalForm):
    class Meta:
        model = Item
        fields = ['item_name', 'price_per_cup', 'price_per_kg', 'price_per_unit']
    