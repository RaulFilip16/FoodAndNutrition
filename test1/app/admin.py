from django.contrib import admin
from .models import *

# Register your models here.

class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'ingredients','meal','grams']
    search_fields=("name","ingredients")
    list_filter=("ingredients",)

class IngredientAdmin(admin.ModelAdmin):
    list_display=['id','name','weight','FoodType','nutrients']



admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredients, IngredientAdmin)
admin.site.register(Nutrient)
admin.site.register(Meal)
admin.site.register(FoodType)