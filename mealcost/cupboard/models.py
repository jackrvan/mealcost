from taggit.managers import TaggableManager

from django.db import models

class Item(models.Model):
    MEAT = "MEAT"
    VEGETABLE = "VEGETABLE"
    FRUIT = "FRUIT"
    DAIRY = "DAIRY"
    GRAIN = "GRAIN"
    FROZEN = "FROZEN"
    OTHER = "OTHER"

    CATEGORY_CHOICES = [
        (MEAT, "Meat"),
        (VEGETABLE, "Vegetable"),
        (FRUIT, "Fruit"),
        (DAIRY, "Dairy"),
        (GRAIN, "Grain"),
        (FROZEN, "Frozen"),
        (OTHER, "Other"),
    ]

    item_name = models.CharField(max_length=100, unique=True)
    price_per_cup = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price_per_kg = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price_per_unit = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return '{}: ${:0.2f}/Cup'.format(self.item_name or "NONE", self.price_per_cup or 0.00)
