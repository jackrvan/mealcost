"""
Django views defined for the cupboard application.
"""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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

def add_item(request):
    if request.method == "POST":
        # We are processing our form data
        form = AddItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['item_name']
            ppc = form.cleaned_data['price_per_cup']
            ppkg = form.cleaned_data['price_per_kg']
            ppu = form.cleaned_data['price_per_unit']
            new_item = Item(item_name=name, price_per_cup=(ppc or None), price_per_kg=(ppkg or None), price_per_unit=(ppu or None))
            new_item.save()
            # Go back to cupboard index page
            return HttpResponseRedirect(reverse('cupboard:index'), {'items_in_cupboard': Item.objects.all()})
    else:
        form = AddItemForm()
        return render(request, 'cupboard/add_item.html', context={"form": form, "categories": [i[1] for i in Item.CATEGORY_CHOICES]})


def item_detail(request, item_name):
    item = get_object_or_404(Item, item_name=item_name)
    return render(request, 'cupboard/item_detail.html', {'item': item})

