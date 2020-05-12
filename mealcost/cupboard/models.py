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
    item_category = models.CharField(choices=CATEGORY_CHOICES, max_length=max(len(i[0]) for i in CATEGORY_CHOICES), default=OTHER)


    def __str__(self):
        return '{}: ${:0.2f}/Cup'.format(self.item_name or "NONE", self.price_per_cup or 0.00)
