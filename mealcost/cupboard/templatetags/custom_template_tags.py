from django import template
from cupboard.models import Item

register = template.Library()

@register.simple_tag
def get_category(category=None):
    return Item.objects.filter(tags__name__in=[category])