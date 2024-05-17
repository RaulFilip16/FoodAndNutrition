from django import forms
from .models import Dish, Meal


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'grams', 'meal']

    def __init__(self, *args, **kwargs):
        all_meals = Meal.objects.all()
        super(DishForm, self).__init__(*args, **kwargs)
        self.fields['meal'].queryset = all_meals
