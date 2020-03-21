# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Book(models.Model):
    collectionid = models.IntegerField(db_column='CollectionID', blank=True, null=True)  # Field name made lowercase.
    bookid = models.TextField(db_column='BookID', blank=True, null=True)  # Field name made lowercase.
    name_en = models.TextField(blank=True, null=True)
    nameshort_en = models.TextField(blank=True, null=True)
    hadith_start = models.IntegerField(blank=True, null=True)
    hadith_end = models.IntegerField(blank=True, null=True)
    hadith_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Book'


class Chapter(models.Model):
    collectionid = models.IntegerField(db_column='CollectionID', blank=True, null=True)  # Field name made lowercase.
    bookid = models.TextField(db_column='BookID', blank=True, null=True)  # Field name made lowercase.
    chapid = models.TextField(db_column='ChapID', blank=True, null=True)  # Field name made lowercase.
    name_en = models.TextField(blank=True, null=True)
    name_ar = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Chapter'


class Collection(models.Model):
    collectionid = models.AutoField(db_column='CollectionID', primary_key=True)  # Field name made lowercase.
    name_en = models.TextField(blank=True, null=True)
    desc_en = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Collection'


class Hadith(models.Model):
    global_id = models.TextField(db_column='global', primary_key=True)  # Field renamed because it was a Python reserved word. This field type is a guess.
    collectionid = models.TextField(db_column='CollectionID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bookid = models.TextField(db_column='BookID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    chapid = models.TextField(db_column='ChapID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hadithidcollection = models.TextField(db_column='HadithIDCollection', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hadithid = models.TextField(db_column='HadithID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    narrator_en = models.TextField(blank=True, null=True)  # This field type is a guess.
    text_en = models.TextField(blank=True, null=True)  # This field type is a guess.
    grade_en = models.TextField(blank=True, null=True)  # This field type is a guess.
    reference_en = models.TextField(blank=True, null=True)  # This field type is a guess.
    related_en = models.TextField(blank=True, null=True)  # This field type is a guess.
    narrator_ar = models.TextField(blank=True, null=True)  # This field type is a guess.
    text_ar = models.TextField(blank=True, null=True)  # This field type is a guess.
    narrator_arend = models.TextField(blank=True, null=True)  # This field type is a guess.
    grade_ar = models.TextField(blank=True, null=True)  # This field type is a guess.
    narrator_ar_diacless = models.TextField(blank=True, null=True)  # This field type is a guess.
    text_ar_diacless = models.TextField(blank=True, null=True)  # This field type is a guess.
    narrator_arend_diacless = models.TextField(blank=True, null=True)  # This field type is a guess.
    grade_ar_diacless = models.TextField(blank=True, null=True)  # This field type is a guess.
    narrators = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'hadith'

class Scholars(models.Model):
    id = models.IntegerField(db_column='Id', unique=True,primary_key=True)  # Field name made lowercase.
    famousname = models.TextField(db_column='famousName', blank=True, null=True)  # Field name made lowercase.
    fullname = models.TextField(db_column='fullName', blank=True, null=True)  # Field name made lowercase.
    othername = models.TextField(db_column='otherName', blank=True, null=True)  # Field name made lowercase.
    rank = models.IntegerField(blank=True, null=True)
    birthdate = models.TextField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
    birthcity = models.TextField(db_column='birthCity', blank=True, null=True)  # Field name made lowercase.
    deathdate = models.TextField(db_column='deathDate', blank=True, null=True)  # Field name made lowercase.
    deathcity = models.TextField(db_column='deathCity', blank=True, null=True)  # Field name made lowercase.
    howdied = models.TextField(db_column='howDied', blank=True, null=True)  # Field name made lowercase.
    livecity = models.TextField(db_column='liveCity', blank=True, null=True)  # Field name made lowercase.
    interests = models.TextField(blank=True, null=True)
    mudhab = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    kunya = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Scholars'


class HadithNarrators(models.Model):
    global_id = models.IntegerField(blank=True, null=True)
    narrator_id = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hadithnarattors'

class RelatedHadiths(models.Model):
    global_id_target = models.IntegerField(db_column='global_id_target')  # Field name made lowercase.
    global_id_related = models.IntegerField(db_column='global_id_related')  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)

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

