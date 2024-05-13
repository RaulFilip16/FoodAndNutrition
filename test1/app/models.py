from django.db import models


# Create your models here.

    # al definir aquest metode nomes li diem a la classe students que tot aquells Objectes Student els veguem pel seu nom es a dir en comptes de Student Object -> Pol
    def __str__(self):
        return self.name


class User(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    # age = models.IntegerField(null = True)
=======


class Meal(models.Model):
    MEALS = [('Esmorzar', 'Esmorzar'),
             ('Dinar', 'Dinar'),
             ('Berenar', 'Berenar'),
             ('Sopar', 'Sopar'),
             ('Altres', 'Altres')]

    name = models.CharField(max_length=20, choices=MEALS, unique=True)
    time = models.TimeField()


    def __str__(self):
        return f"{self.name} | {self.time}"


class Dish(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.ForeignKey('Ingredients', null=True, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    weight = models.IntegerField(null=True)
    FoodType = models.OneToOneField('FoodType', null=True, on_delete=models.CASCADE)
    nutrients = models.OneToOneField('Nutrient', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.weight} gr"


class FoodType(models.Model):
    FOODTYPE = [('Carn', 'Carn'),
                ('Peix', 'Peix'),
                ('Ous', 'Ous'),
                ('Fruita', 'Fruita'),
                ('Verdura', 'Verdura'),
                ('Pasta', 'Pasta')]

    name = models.CharField(max_length=20, choices=FOODTYPE, unique=True)

    def __str__(self) -> str:
        return self.name


class Nutrient(models.Model):
    calories = models.FloatField(null=True)
    protein = models.FloatField(null=True)
    carbos = models.FloatField(null=True)
    grasa = models.FloatField(null=True)
    grasaSAT = models.FloatField(null=True)

    def __str__(self) -> str:
        return f"{self.calories} kcal | PROT: {self.protein} gr | CARB: {self.carbos} gr | GRAS: {self.grasa} gr | GRASsat: {self.grasaSAT} gr"
