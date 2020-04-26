from django.db import models

from cupboard.models import Item


class ItemRecipeJunction(models.Model):
    recipe = models.ForeignKey('recipe.Recipe', on_delete=models.CASCADE)
    item = models.ForeignKey('cupboard.Item', on_delete=models.CASCADE)    
    cups_of_item = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    kgs_of_item = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    units_of_item = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.item.item_name} is in {self.recipe.recipe_name}'


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, unique=True)
    ingredients = models.ManyToManyField(Item, through=ItemRecipeJunction, related_name="is_in")

    def __str__(self):
        return '{}'.format(self.recipe_name)


