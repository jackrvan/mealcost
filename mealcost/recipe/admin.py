from django.contrib import admin

# Register your models here.
from .models import ItemRecipeJunction, Recipe

admin.site.register(ItemRecipeJunction)
admin.site.register(Recipe)
