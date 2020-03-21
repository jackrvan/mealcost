from django.db import models

# Create your models here.
from cupboard.models import Item


class Recipe(models.Model):
    ingredient_name = models.ForeignKey(Item, on_delete=models.CASCADE)
