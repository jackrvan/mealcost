from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=100, unique=True)
    price_per_cup = models.DecimalField(max_digits=7, decimal_places=2)
    price_per_kg = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return '{}: ${}/Cup'.format(self.item_name, self.price_per_cup)
