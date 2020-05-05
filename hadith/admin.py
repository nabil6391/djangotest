from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV

from hadith.models import Book, Chapter, Collection,  Hadith

# class HadithNarratorInline(admin.TabularInline):
#     model = HadithNarrators
#     extra = 1
#
# class RelatedHadithInline(admin.TabularInline):
#     model = RelatedHadiths
#     fk_name = "hadith_target"
#     extra = 1

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    pass

@admin.register(Collection)
class CollectionAdmin(ImportExportModelAdmin):
    pass

@admin.register(Chapter)
class ChapterAdmin(ImportExportModelAdmin):
    pass

# @admin.register(Scholars)
# class ScholarsAdmin(ImportExportModelAdmin):
#     # inlines = (HadithNarratorInline,)
#     pass

@admin.register(Hadith)
class HadithAdmin(ImportExportModelAdmin):
    # readonly_fields = ('related_en','narrators_en')
    # inlines = (HadithNarratorInline, RelatedHadithInline)
    pass
#
# @admin.register(HadithNarrators)
# class HadithNarratorsAdmin(ImportExportModelAdmin):
#     pass
#
# @admin.register(RelatedHadiths)
# class RelatedHadithsAdmin(ImportExportModelAdmin):
#     pass

