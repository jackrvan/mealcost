from django.db import models

from cupboard.models import Item

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '{}'.format(self.recipe_name)

class ItemRecipeJunction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="is_in")
    cups_of_item = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    kgs_of_item = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    units_of_item = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.item.item_name} is in {self.recipe.recipe_name}'
