from collections import defaultdict

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView

from cupboard.models import Item
from recipe.forms import AddRecipeForm
from recipe.models import ItemRecipeJunction
from recipe.parse_recipes import parse_recipe_url
from recipe.constants import KNOWN_UNITS

from .models import Recipe


# Create your views here.
class IndexView(ListView):
    """View defined for Recipe index page.
    """
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipe/index.html'


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe:index')


class DetailView(DetailView):
    """View defined for the Recipe detail page. 
    """
    model = Recipe
    template_name = 'recipe/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['recipe'] = self.object
        recipe = self.object

        ingredients = {}
        price = 0.0
        for i in recipe.ingredients.all():
            print("i = {}".format(i))
            # Get all ingredients in the current recipe
            j = ItemRecipeJunction.objects.get(recipe=recipe, item=i)
            print('j = {}'.format(j))

            if j.cups_of_item and i.price_per_cup:
                price += (float(j.cups_of_item) * float(i.price_per_cup))
                ingredients[i] = ('Cup', j.cups_of_item)
            elif j.kgs_of_item and i.price_per_kg:
                price += (float(j.kgs_of_item) * float(i.price_per_kg))
                ingredients[i] = ('Kg', j.kgs_of_item)
            elif j.units_of_item and i.price_per_unit:
                price += (float(j.units_of_item) * float(i.price_per_unit))
                ingredients[i] = ('Unit', j.units_of_item)
            else:
                units_specified = "Cup" if j.cups_of_item else ("Kg" if j.kgs_of_item else ("Unit" if j.units_of_item else ""))
                prices_specified = i.price_per_cup or i.price_per_kg or i.price_per_unit or 0.0
                print("units = {}, price = {}".format(units_specified, prices_specified))
                ingredients[i] = (units_specified, prices_specified)
#                context['price_error'] = "Could not calculate price of recipe because youve only specified {} for item amount and only {} for price".format(units_specified, prices_specified)
        context['ingredients'] = ingredients
        context['price'] = '{:.2f}'.format(price)
        return context

def add_recipe(request):
    def save_to_database(request, name):
        """Given a request and a recipe name add the new recipe to our database

        Args:
            request (HttpRequest): Contains our ingredient information
            name (str): name of our new recipe
        """
        new_recipe = Recipe(recipe_name=name)
        new_recipe.save()

        # Create a new ItemRecipeJunction based on each ingredient we have in our recipe
        ingredients = Item.objects.all()
        for ingredient in ingredients:
            name = ingredient.item_name
            amount = request.POST[f"{name}_amount"].strip()
            if not amount:
                continue
            measurement = request.POST[f"{name}_measurement"]
            ingredient = Item.objects.get(item_name=name)
            if measurement == "cups":
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=ingredient, cups_of_item=amount)
            elif measurement == "kgs":
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=ingredient, kgs_of_item=amount)
            elif measurement == "units":
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=ingredient, units_of_item=amount)
            new_junction.save()

    if request.method == "POST":
        # We are processing our form data
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["recipe_name"]
            save_to_database(request, name)
            return HttpResponseRedirect(reverse('recipe:index'), {'recipe': Recipe.objects.all()})
    else:
        form  = AddRecipeForm()
        return render(request, 'recipe/add_recipe.html', context={"form": form, "ingredients": Item.objects.all()})

def add_recipe_from_url(request):
    def save_to_database_from_url(request, name):
        """Given a request and a recipe name add the new recipe to our database

        Args:
            request (HttpRequest): Contains our URL
            name (str): name of our new recipe
        """
        new_recipe = Recipe(recipe_name=name)
        new_recipe.save()

        ingredient_list = parse_recipe_url(request.POST['url-input'])
        print('\n'.join(ingredient_list))
        for ingredient in ingredient_list:
            amount = ingredient.split()[0]
            if not amount.isnumeric():
                item_name = ingredient
                amount = 1
            else:
                unit = ingredient.split()[1]
                if unit in KNOWN_UNITS:
                    item_name = ' '.join(ingredient.split()[2:])
                else:
                    item_name = ' '.join(ingredient.split()[1:])
            try:
                item = Item.objects.get(item_name=item_name)
            except Item.DoesNotExist:
                item = Item(item_name=item_name, price_per_cup=0, price_per_kg=0, price_per_unit=0, category=Item.OTHER)
                item.save()
            if unit in ('cup', 'cups'):
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=item, cups_of_item=amount)
            elif unit in ('tbsp', 'tablespoon', 'tablespoons'):
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=item, cups_of_item=round(float(amount)/16.0, 2))
            elif unit in ('tsp', 'teaspoon', 'teaspoons'):
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=item, cups_of_item=round(float(amount)/48.0, 2))
            elif unit in ('kgs', 'kg'):
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=item, kgs_of_item=amount)
            elif unit in ('g', 'gram', 'grams'):
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=item, kgs_of_item=round(float(amount)*1000, 2))
            elif unit in ('lbs', 'pound', 'pounds'):
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=item, kgs_of_item=round(float(amount)*2.2, 2))
            elif unit not in KNOWN_UNITS:
                print("NOT RECOGNIZING unit {} so just treating item {} as a unit".format(unit, item))
                new_junction = ItemRecipeJunction(recipe=new_recipe, item=item, units_of_item=amount)
            else:
                print("Something went wrong with ingredient {}. Got amount {}, unit {}, item {}".format(ingredient, amount, unit, item))
                continue
            new_junction.save()

    if request.method == "POST":
        # We are processing our form data
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["recipe_name"]
            save_to_database_from_url(request, name)
            return HttpResponseRedirect(reverse('recipe:index'), {'recipe': Recipe.objects.all()})
    else:
        form  = AddRecipeForm()
        return render(request, 'recipe/add_recipe_from_url.html', context={"form": form})

