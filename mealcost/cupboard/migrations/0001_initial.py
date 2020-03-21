# Generated by Django 3.0.3 on 2020-03-06 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('price_per_cup', models.DecimalField(decimal_places=2, max_digits=7)),
                ('price_per_kg', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
