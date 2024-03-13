from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    age = models.IntegerField(blank=True, null=True)

    # al definir aquest metode nomes li diem a la classe students que tot aquells Objectes Student els veguem pel seu nom es a dir en comptes de Student Object -> Pol
    def __str__(self):
        return self.name

class User(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

class Dish(models.Model):
    name = models.CharField(max_length=30)
    ingredients = models.ManyToManyField('Ingredients')

    def __str__(self):
        return self.name
    
class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    pes = models.IntegerField()
    # dish = models.ManyToManyField(Dish,related_name='Ingredients')

    def __str__(self):
        return self.name
    

    
class Nutrient(models.Model):

    # ingredient = models.ForeignKey(Ingredients, on_delete = models.CASCADE, related_name='nutrients')
    NUTRIENTS = [('Calorias','Calorias'),
                 ('Proteina','Proteina'),
                 ('Grasas','Grasas'),
                 ('Carbohidratos','Carbohidratos'),
                 ('Sal','Sal')]
    
    name = models.CharField(max_length=20, choices=NUTRIENTS, unique=True )
    quantity = models.IntegerField()

    def __str__(self):
        return self.name





