from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from cupboard.models import Item
from recipe.models import ItemRecipeJunction

from .models import Recipe


# Create your views here.
class Index(generic.ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipe/index.html'


def add_recipe(request):
    ingredients = Item.objects.all()
    context = {'ingredients': ingredients}
    return render(request, 'recipe/add_recipe.html', context)


def recipe_details(request, recipe_name):
    recipe = get_object_or_404(Recipe, recipe_name=recipe_name)
    ingredients = [i for i in recipe.ingredients.all()]
    context = {
        'recipe': recipe,
        'ingredients': ingredients
        }
    return render(request, 'recipe/recipe_detail.html', context)


def add_recipe_form(request):
    name = request.POST['recipe_name']
    ingredient_ids = request.POST.getlist('ingredients')
    new_recipe = Recipe(recipe_name=name)
    new_recipe.save()
    for _id in ingredient_ids:
        ingredient = Item.objects.get(id=_id)
        new_junction = ItemRecipeJunction(recipe=new_recipe, item=ingredient)
        new_junction.save()
    return HttpResponseRedirect(reverse('recipe:index'), {'recipe': Recipe.objects.all()})
