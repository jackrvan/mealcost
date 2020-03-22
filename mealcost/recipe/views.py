from django.shortcuts import render
from django.views import generic

from .models import Recipe


# Create your views here.
class Index(generic.ListView):
    model = Recipe
    context_object_name = 'recipe_ingredients'
    template_name = 'recipe/index.html'
