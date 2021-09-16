# Generated by Django 2.1.11 on 2021-08-28 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cupboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('DAIRY', 'Dairy'), ('FRUIT', 'Fruit'), ('GRAIN', 'Grain'), ('MEAT', 'Meat'), ('FROZEN', 'Frozen'), ('VEGETABLE', 'Vegetable'), ('OTHER', 'Other')], default='OTHER', max_length=10),
        ),
    ]
