# Generated by Django 2.1.11 on 2020-05-18 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cupboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRecipeJunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cups_of_item', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('kgs_of_item', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('units_of_item', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cupboard.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100, unique=True)),
                ('ingredients', models.ManyToManyField(related_name='is_in', through='recipe.ItemRecipeJunction', to='cupboard.Item')),
            ],
        ),
        migrations.AddField(
            model_name='itemrecipejunction',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe'),
        ),
    ]
