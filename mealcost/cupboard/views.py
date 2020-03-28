"""
Django views defined for the cupboard application.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import FormView

from .models import Item
from .forms import AddItemForm


class Index(generic.ListView):
    model = Item
    context_object_name = 'items_in_cupboard'
    template_name = 'cupboard/index.html'


def add_item(request):
    return render(request, 'cupboard/add_item.html')


def item_detail(request, item_name):
    item = get_object_or_404(Item, item_name=item_name)
    return render(request, 'cupboard/item_detail.html', {'item': item})


def add_item_form(request):
    name = request.POST['item_name']
    ppc = request.POST['price_per_cup']
    ppkg = request.POST['price_per_kg']
    ppu = request.POST['price_per_unit']
    new_item = Item(item_name=name, price_per_cup=ppc, price_per_kg=ppkg, price_per_unit=ppu)
    new_item.save()
    return HttpResponseRedirect(reverse('cupboard:index'), {'items_in_cupboard': Item.objects.all()})
