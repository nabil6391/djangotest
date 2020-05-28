# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from incubator.models import User

class Collection(models.Model):
    collectionid = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=1000)
    desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Collection'

    def __str__(self):
        return self.name
        pass



class Book(models.Model):
    Collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    bookid = models.CharField(blank=True, null=True, max_length=1000)  
    name = models.CharField(blank=True, null=True, max_length=1000)
    nameshort_en = models.CharField(blank=True, null=True, max_length=1000)
    hadith_start = models.PositiveIntegerField(blank=True, null=True)
    hadith_end = models.PositiveIntegerField(blank=True, null=True)
    hadith_count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Book'

    def __str__(self):
        return self.name
        pass


class Chapter(models.Model):
    Collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Chap = models.CharField(blank=True, null=True, max_length=10)
    name_en = models.CharField(blank=True, null=True, max_length=1000)
    name_ar = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        managed = True
        db_table = 'Chapter'

    def __str__(self):
        return self.name
        pass



class Hadith(models.Model):
    global_id = models.AutoField(primary_key=True)
    Collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Chap = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)
    hadith_no = models.PositiveIntegerField(blank=True, null=True)
    narrator = models.CharField(blank=True, null=True, max_length=100)
    text = models.TextField(default="")
    narrator_ar = models.CharField(blank=True, null=True, max_length=100)
    text_ar = models.TextField(default="")
    grade =  models.CharField(blank=True, null=True, max_length=100)
    reference = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hadith'

    def __str__(self):
        return self.Collection.name +" "+ self.Book.name +" "+ str(self.hadithid)
        pass

#


