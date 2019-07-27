from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import CSV

from incubator.models import SeerahTopic, App, AppLike, Dictionary, SeerahQuestion, User


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    readonly_fields = ('id',)
    pass


@admin.register(App)
class AppAdmin(ImportExportModelAdmin):
    list_display = ( 'name', 'likes')
    readonly_fields = ('id',)
    pass


@admin.register(AppLike)
class AppLikesAdmin(ImportExportModelAdmin):
    readonly_fields = ('id',)
    pass



@admin.register(Dictionary)
class DictionaryAdmin(ImportExportModelAdmin):
    readonly_fields = ('id',)
    list_display = ('word', 'word_diacless', 'description')
    pass


@admin.register(SeerahTopic)
class SeerahTopicAdmin(ImportExportModelAdmin):
    readonly_fields = ('id',)
    pass


@admin.register(SeerahQuestion)
class SeerahQuestionAdmin(ImportExportModelAdmin):
    list_display = ('topic_id', 'question', 'answer')
    fields = ('topic_id', 'question', 'answer')
    pass


class DictionaryResource(resources.ModelResource):

    class Meta:
        model = Dictionary
        fields = ('topic_id', 'question', 'answer')

    pass


class SeerahQuestionResource(resources.ModelResource):

    class Meta:
        model = SeerahQuestion
        fields = ('topic_id', 'question', 'answer')

    pass


class SeerahTopicResource(resources.ModelResource):

    class Meta:
        model = SeerahTopic
        fields = ('topic_id', 'name')
    pass