
from django import forms
from .models import Dish, Meal, Ingredients


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'meal', 'ingredients']


    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)
        self.fields['meal'].queryset = Meal.objects.all()
        self.fields['ingredients'].queryset = Ingredients.objects.all()