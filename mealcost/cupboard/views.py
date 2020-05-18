"""
Django views defined for the cupboard application.
"""

from collections import defaultdict

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import AddItemForm
from .models import Item


class Index(generic.ListView):
    """View defined for Cupboard index page.
    """
    model = Item
    template_name = 'cupboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['categories'] = sorted(Item.tags.all())
        context['items_with_no_tags'] = [i for i in Item.objects.all() if not i.tags.all()]   # Collect items that do not have a tag
        return context

class DetailView(generic.DetailView):
    """View defined for the Cupboard detail page. 
    """
    model = Item
    template_name = 'cupboard/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['recipes'] = [r for r in self.object.is_in.all()]
        return context

class AddItemView(generic.CreateView):
    template_name = "cupboard/add_item.html"
    form_class = AddItemForm
    success_url = reverse_lazy("cupboard:index")
