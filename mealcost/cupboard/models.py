
from django.db import models

class Item(models.Model):
    DAIRY = "DAIRY"
    FRUIT = "FRUIT"
    GRAIN = "GRAIN"
    MEAT = "MEAT"
    FROZEN = "FROZEN"
    VEGETABLE = "VEGETABLE"
    OTHER = "OTHER"

    CATEGORY_CHOICES = [
        (DAIRY, "Dairy"),
        (FRUIT, "Fruit"),
        (GRAIN, "Grain"),
        (MEAT, "Meat"),
        (FROZEN, "Frozen"),
        (VEGETABLE, "Vegetable"),
        (OTHER, "Other"),
    ]

    item_name = models.CharField(max_length=100, unique=True)
    price_per_cup = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price_per_kg = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    price_per_unit = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=OTHER)

    def __str__(self):
        return '{}: ${:0.2f}/Cup'.format(self.item_name or "NONE", self.price_per_cup or 0.00)
