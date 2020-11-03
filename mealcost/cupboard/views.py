"""
Django views defined for the cupboard application.
"""

from collections import defaultdict

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from .forms import AddItemForm
from .models import Item

from bootstrap_modal_forms.generic import BSModalCreateView

class Index(ListView):
    """View defined for Cupboard index page.
    """
    model = Item
    template_name = 'cupboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['categories'] = [x[1] for x in Item.CATEGORY_CHOICES]  # Get list of all categories
        return context

class DetailView(DetailView):
    """View defined for the Cupboard detail page. 
    """
    model = Item
    template_name = 'cupboard/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['recipes'] = [r for r in self.object.is_in.all()]
        return context

class AddItemView(BSModalCreateView):
    template_name = "cupboard/add_item.html"
    form_class = AddItemForm
    success_url = reverse_lazy("cupboard:index")

class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('cupboard:index')
