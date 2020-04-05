from django.test import TestCase
from django.urls import reverse

from mealcost.create_objects_for_tests import *

class RecipeModelTests(TestCase):
    def test_cupboard_str_output(self):
        recipe = create_recipe("test_recipe")
        self.assertEqual(str(recipe), 'test_recipe')

    def test_junction_str_output(self):
        recipe = create_recipe("test_recipe")
        item = create_item(item_name="fake_item", ppc=1.9876)
        junction = create_junction(recipe=recipe, item=item)
        self.assertEqual(str(junction), 'fake_item is in test_recipe')


class RecipeIndexViewTests(TestCase):
    def test_no_recipes(self):
        response = self.client.get(reverse('recipe:index'))
        self.assertEqual(response.status_code, 200)  # it exists
        self.assertContains(response, "You do not have any saved recipes.")
        self.assertQuerysetEqual(response.context['recipes'], [])

    def test_with_recipe(self):
        create_recipe("test_recipe")
        response = self.client.get(reverse('recipe:index'))
        self.assertQuerysetEqual(response.context['recipes'], ['<Recipe: test_recipe>'])

class RecipeDetailViewTests(TestCase):
    def test_recipe_with_no_ingredients(self):
        recipe = create_recipe("test_recipe")
        response = self.client.get(reverse('recipe:detail', args=(recipe.id,)))
        self.assertContains(response, 'This recipe has no ingredients')
    
    def test_recipe_with_ingredients(self):
        item1 = create_item("item_in_recipe")
        create_item("item_not_in_recipe")
        recipe = create_recipe("fake_recipe")
        create_junction(recipe, item1)
        response = self.client.get(reverse('recipe:detail', args=(recipe.id,)))
        self.assertContains(response, 'item_in_recipe')
        self.assertNotContains(response, 'item_not_in_recipe')
