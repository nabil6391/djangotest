from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV

from hadith.models import Book, Chapter, Collection, Scholars, HadithNarrators, Hadith, RelatedHadiths


@admin.register(Book)
class UserAdmin(ImportExportModelAdmin):

    pass


@admin.register(Collection)
class AppLikesAdmin(ImportExportModelAdmin):
    pass

@admin.register(Chapter)
class DictionaryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Scholars)
class SeerahTopicAdmin(ImportExportModelAdmin):
    pass


@admin.register(Hadith)
class SeerahQuestionAdmin(ImportExportModelAdmin):
    pass

@admin.register(HadithNarrators)
class SeerahQuestionAdmin(ImportExportModelAdmin):
    pass

@admin.register(RelatedHadiths)
class SeerahQuestionAdmin(ImportExportModelAdmin):
    pass

