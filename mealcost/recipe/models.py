from django.db import models

# Create your models here.
from cupboard.models import Item


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, unique=True)
    # Lets explicitly state through even though we could use the django default
    ingredients = models.ManyToManyField(
        Item,
        through="ItemRecipeJunction",
        through_fields=('recipe', 'item')
    )

    def __str__(self):
        return self.recipe_name

class ItemRecipeJunction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
