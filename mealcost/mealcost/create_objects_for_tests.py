from recipe.models import Recipe, ItemRecipeJunction
from cupboard.models import Item


def create_recipe(recipe_name):
    return Recipe.objects.create(recipe_name=recipe_name)

def create_junction(recipe, item, c_of_item=None, kg_of_item=None, u_of_item=None):
    return ItemRecipeJunction.objects.create(item=item, recipe=recipe, cups_of_item=c_of_item, kgs_of_item=kg_of_item, units_of_item=u_of_item)

def create_item(item_name, ppc=None, ppkg=None, ppu=None):
    return Item.objects.create(item_name=item_name, price_per_cup=ppc, price_per_kg=ppkg, price_per_unit=ppu)
