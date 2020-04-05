from django.test import TestCase
from django.urls import reverse

from mealcost.create_objects_for_tests import *


class CupboardModelTests(TestCase):
    def test_item_str_output(self):
        item = create_item(item_name="fake_item", ppc=1.9876)
        self.assertEqual(str(item), "fake_item: $1.99/Cup")


class CupboardIndexViewTests(TestCase):
    def test_no_items(self):
        response = self.client.get(reverse('cupboard:index'))
        self.assertEqual(response.status_code, 200)  # it exists
        self.assertContains(response, "You do not have any items in your cupboard.")
        self.assertQuerysetEqual(response.context['items_in_cupboard'], [])

    def test_with_item(self):
        create_item("fake_item")
        response = self.client.get(reverse('cupboard:index'))
        self.assertContains(response, "fake_item")
        self.assertNotContains(response, "You do not have any items in your cupboard.")
        self.assertQuerysetEqual(response.context['items_in_cupboard'], ['<Item: fake_item: $0.00/Cup>'])


class CupboardDetailViewTests(TestCase):
    def test_non_existant_item(self):
        response = self.client.get(reverse('cupboard:detail', args=(1,)))
        self.assertEqual(response.status_code, 404)  #  We have non items so id 1 should not exist
    
    def test_item_not_in_any_recipes(self):
        item = create_item('fake_item')
        response = self.client.get(reverse('cupboard:detail', args=(item.id,)))
        self.assertContains(response, 'This item is not a part of any saved recipes.')
    
    def test_item_that_is_in_recipe(self):
        item = create_item('fake_item')
        recipe = create_recipe('item_in_recipe')
        create_recipe('item_not_in_recipe')
        create_junction(recipe, item)
        response = self.client.get(reverse('cupboard:detail', args=(item.id,)))
        self.assertContains(response, "item_in_recipe")
        self.assertNotContains(response, "item_not_in_recipe")
