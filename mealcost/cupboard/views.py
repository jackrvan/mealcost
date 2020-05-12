"""
Django views defined for the cupboard application.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Item
from .forms import AddItemForm


class Index(generic.ListView):
    """View defined for Cupboard index page.
    """
    model = Item
    context_object_name = 'items_in_cupboard'
    template_name = 'cupboard/index.html'


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
