# Generated by Django 5.0.1 on 2024-03-13 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_dish_ingredients_dish_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='FoodType',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.foodtype'),
        ),
    ]