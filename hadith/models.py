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
    name_en = models.CharField(blank=True, null=True, max_length=1000)
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

# related_hadiths = models.ManyToManyField('self',through='RelatedHadiths',symmetrical=False)
    # narrators = models.ManyToManyField('Scholars',through='HadithNarrators',blank = True)

    class Meta:
        managed = True
        db_table = 'hadith'

    # def related(self):
    #     return self.related_hadiths.all()
    #     pass
    #
    # def narrators(self):
    #     return self.narrators.all()
    #     pass

    def __str__(self):
        return self.Collection.name +" "+ self.Book.name +" "+ str(self.hadithid)
        pass

#



# class HadithNarrators(models.Model):
#     hadith = models.ForeignKey(Hadith, on_delete=models.CASCADE)
#     narrator = models.ForeignKey(Scholars, on_delete=models.CASCADE)
#     position = models.PositiveIntegerField(blank=True, null=True,validators=[MinValueValidator(0),
#                                                                 MaxValueValidator(5)])
#     accuracy = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'hadithnarattors'
#         constraints = [
#             models.UniqueConstraint(fields=['hadith', 'narrator'], name='Hadith and Narrator are unique together')
#         ]
#
#     def __str__(self):
#         return self.hadith.__str__() + " : "+ self.narrator.famousname
#         pass

# class RelatedHadiths(models.Model):
#     hadith_target = models.ForeignKey(Hadith, on_delete=models.CASCADE,related_name='global_id_target')
#     hadith_related = models.ForeignKey(Hadith, on_delete=models.CASCADE,related_name='global_id_related')
#     type = models.PositiveIntegerField(blank=True, null=True)
#     accuracy = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'relatedhadiths'
#         constraints = [
#                     models.UniqueConstraint(fields=['hadith_target', 'hadith_related'], name='Hadith and User are unique together'),
#                 ]
#
#     def __str__(self):
#         return self.hadith_target.__str__() + " : "+ self.hadith_related.__str__()
#         pass


# crowdsourced data
# class NarratorSuggestion(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     hadith = models.ForeignKey(Hadith, on_delete=models.CASCADE)
#     narrator = models.ForeignKey(Scholars, on_delete=models.CASCADE)
#     position = models.PositiveIntegerField(blank=True, null=True,validators=[MinValueValidator(0),
#                                                                              MaxValueValidator(5)])
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['hadith', 'user','narrator'], name='Hadith and User are unique together')
#         ]
#
#     def __str__(self):
#         return str(self.user.id) + " likes " + self.hadith
#
#     pass
# #
# class RelatedHadithSuggestion(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     hadith = models.ForeignKey(Hadith, on_delete=models.CASCADE)
#     narrator = models.ForeignKey(Scholars, on_delete=models.CASCADE)
#
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['user', 'hadith','narrator'], name='Hadith and User are unique together')
#         ]
#
#     def __str__(self):
#         return str(self.user.id) + " likes " + self.Hadith.name
#
#     pass
# #
