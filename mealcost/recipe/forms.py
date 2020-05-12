from django import forms
from django.forms.widgets import CheckboxSelectMultiple, RadioSelect

from recipe.models import ItemRecipeJunction

from .models import Recipe


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name']
