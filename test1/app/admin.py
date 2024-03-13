from django.contrib import admin
from .models import *

# Register your models here.

class DishAdmin(admin.ModelAdmin):
     # en aquesta classe li podem indicar quins valors podem veure al superuser quan veiem cada objecte
    list_display = ['id','name', 'ingredients','meal']
    #metode per a buscar o fer quaerys
    search_fields=("name","ingredients")
    #metode per a filtrar, basicament te pose al usuari el panel a la dreta per filtrar  
    list_filter=("ingredients",)

class IngredientAdmin(admin.ModelAdmin):
    list_display=['id','name','weight','FoodType','nutrients']


admin.site.register(Student)
admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredients, IngredientAdmin)
admin.site.register(Nutrient)
admin.site.register(Meal)
admin.site.register(FoodType)