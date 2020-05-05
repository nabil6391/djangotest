from rest_framework.serializers import ModelSerializer
from hadith.models import Book, Chapter, Collection, Hadith


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class ChapterSerializer(ModelSerializer):

    class Meta:
        model = Chapter
        fields = '__all__'


class CollectionSerializer(ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'


class HadithSerializer(ModelSerializer):

    class Meta:
        model = Hadith
        fields = '__all__'
