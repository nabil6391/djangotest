# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Collection(models.Model):
    collectionid = models.AutoField(db_column='CollectionID', primary_key=True)  
    name_en = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Collection'


class Book(models.Model):
    collectionid = models.ForeignKey(Collection, on_delete=models.CASCADE)  
    bookid = models.CharField(blank=True, null=True, max_length=1000)  
    name_en = models.CharField(blank=True, null=True, max_length=1000)
    nameshort_en = models.CharField(blank=True, null=True, max_length=1000)
    hadith_start = models.IntegerField(blank=True, null=True)
    hadith_end = models.IntegerField(blank=True, null=True)
    hadith_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Book'


class Chapter(models.Model):
    collectionid = models.ForeignKey(Collection, on_delete=models.CASCADE)  
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)  
    chapid = models.CharField(blank=True, null=True, max_length=10)  
    name_en = models.CharField(blank=True, null=True, max_length=1000)
    name_ar = models.CharField(blank=True, null=True, max_length=1000)

    class Meta:
        managed = True
        db_table = 'Chapter'


class Hadith(models.Model):
    global_id = models.TextField(db_column='global_id', primary_key=True) 
    collectionid = models.ForeignKey(Collection, on_delete=models.CASCADE)  
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapid = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    hadithidcollection = models.CharField(blank=True, null=True, max_length=10)
    hadithid = models.CharField(blank=True, null=True, max_length=10)
    narrator_en = models.TextField(blank=True, null=True)  
    text_en = models.TextField(blank=True, null=True)  
    grade_en =  models.CharField(blank=True, null=True, max_length=100)
    reference_en = models.TextField(blank=True, null=True)  
    narrator_ar = models.TextField(blank=True, null=True)  
    text_ar = models.TextField(blank=True, null=True)  
    narrator_arend = models.TextField(blank=True, null=True)  
    grade_ar = models.CharField(blank=True, null=True, max_length=100)
    narrator_ar_diacless = models.TextField(blank=True, null=True)  
    text_ar_diacless = models.TextField(blank=True, null=True)  
    narrator_arend_diacless = models.TextField(blank=True, null=True)  
    grade_ar_diacless =  models.CharField(blank=True, null=True, max_length=100)
    
    related_en = models.TextField(blank=True, null=True)
    narrators = models.TextField(blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'hadith'


class Scholars(models.Model):
    id = models.IntegerField(db_column='Id', unique=True, primary_key=True)  
    famousname = models.CharField(blank=True, null=True, max_length=1000)
    fullname = models.CharField(blank=True, null=True, max_length=1000)
    othername = models.CharField(blank=True, null=True, max_length=1000)
    rank = models.IntegerField(blank=True, null=True)
    birthdate = models.CharField(blank=True, null=True, max_length=1000)
    birthcity = models.CharField(blank=True, null=True, max_length=1000)
    deathdate = models.CharField(blank=True, null=True, max_length=1000)
    deathcity = models.CharField(blank=True, null=True, max_length=1000)
    howdied = models.CharField(blank=True, null=True, max_length=1000)
    livecity = models.CharField(blank=True, null=True, max_length=1000)
    interests = models.CharField(blank=True, null=True, max_length=1000)
    mudhab = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    kunya = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Scholars'


class HadithNarrators(models.Model):
    global_id = models.ForeignKey(Hadith, on_delete=models.CASCADE)
    narrator_id = models.ForeignKey(Scholars, on_delete=models.CASCADE)
    position = models.IntegerField(blank=True, null=True,validators=[MinValueValidator(0),
                                                                MaxValueValidator(5)])
    accuracy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hadithnarattors'


class RelatedHadiths(models.Model):
    global_id_target = models.ForeignKey(Hadith, on_delete=models.CASCADE,related_name='global_id_target')
    global_id_related = models.ForeignKey(Hadith, on_delete=models.CASCADE,related_name='global_id_related')
    type = models.IntegerField(blank=True, null=True)
    accuracy = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'relatedhadiths'

# crowdsourced data
# class NarratorSuggestion(models.Model):
#     app = models.ForeignKey(App, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['app', 'user'], name='App and User are unique together')
#         ]
#
#     def __str__(self):
#         return str(self.user.id) + " likes " + self.app.name
#
#     pass
#
# class RelatedHadithSuggestion(models.Model):
#     app = models.ForeignKey(App, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['app', 'user'], name='App and User are unique together')
#         ]
#
#     def __str__(self):
#         return str(self.user.id) + " likes " + self.app.name
#
#     pass
#
# class RelatedHadithSuggestion(models.Model):
#     app = models.ForeignKey(App, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['app', 'user'], name='App and User are unique together')
#         ]
#
#     def __str__(self):
#         return str(self.user.id) + " likes " + self.app.name
#
#     pass
