from rest_framework.serializers import ModelSerializer
from hadith.models import Book, Chapter, Collection, Hadith, Scholars, HadithNarrators, RelatedHadiths


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


class ScholarsSerializer(ModelSerializer):

    class Meta:
        model = Scholars
        fields = '__all__'


class HadithNarratorsSerializer(ModelSerializer):

    class Meta:
        model = HadithNarrators
        fields = '__all__'


class RelatedHadithsSerializer(ModelSerializer):

    class Meta:
        model = RelatedHadiths
        fields = '__all__'
