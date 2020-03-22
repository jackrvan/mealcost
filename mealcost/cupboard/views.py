"""
Django views defined for the cupboard application.
"""

from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from bootstrap_modal_forms.generic import BSModalCreateView

from .forms import AddItemForm
from .models import Item


class Index(generic.ListView):
    model = Item
    context_object_name = 'items_in_cupboard'
    template_name = 'cupboard/index.html'

'''
def index(request):
    items_in_cupboard = Item.objects.all()
    context = {
        'items_in_cupboard': items_in_cupboard,
    }
    return render(request, 'cupboard/index.html', context)
'''

def item_detail(request, item_name):
    item = get_object_or_404(Item, item_name=item_name)
    return render(request, 'cupboard/item_detail.html', {'item': item})


class ItemAddView(BSModalCreateView):
    template_name = 'cupboard/add_item.html'
    form_class = AddItemForm
    success_message = 'Success: Added item'
    success_url = reverse_lazy('cupboard:index')
