# Generated by Django 5.0.1 on 2024-03-13 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_foodtype_meal_remove_nutrient_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredients',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ingredients'),
        ),
    ]
