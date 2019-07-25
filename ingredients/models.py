from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField()
    category = models.ForeignKey(Category, models.CASCADE, "ingredients")

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
