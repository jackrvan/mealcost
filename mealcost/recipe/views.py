from collections import defaultdict

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from cupboard.models import Item
from recipe.models import ItemRecipeJunction

from .models import Recipe


# Create your views here.
class IndexView(generic.ListView):
    """View defined for Recipe index page.
    """
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipe/index.html'


class DetailView(generic.DetailView):
    """View defined for the Recipe detail page. 
    """
    model = Recipe
    template_name = 'recipe/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['recipe'] = self.object
        # Get all ingredients in the current recipe
        ingredients = (i for i in context['recipe'].ingredients.all())
        context['ingredients'] = ingredients
        return context


def add_recipe(request):
    ingredients = Item.objects.all()
    context = {'ingredients': ingredients}
    return render(request, 'recipe/add_recipe.html', context)


def add_recipe_form(request):
    # Add new recipe
    name = request.POST['recipe_name']
    new_recipe = Recipe(recipe_name=name)
    new_recipe.save()

    # Create a new ItemRecipeJunction based on each ingredient we have in our recipe
    ingredients = Item.objects.all()
    for ingredient in ingredients:
        name = ingredient.item_name
        cups = request.POST[f"{name}_cups"].strip()
        kgs = request.POST[f"{name}_kgs"].strip()
        units = request.POST[f"{name}_units"].strip()
        if cups or kgs or units:
            ingredient = Item.objects.get(item_name=name)
            new_junction = ItemRecipeJunction(recipe=new_recipe, item=ingredient, cups_of_item=(cups or None), kgs_of_item=(kgs or None), units_of_item=(units or None))
            new_junction.save()
    return HttpResponseRedirect(reverse('recipe:index'), {'recipe': Recipe.objects.all()})
