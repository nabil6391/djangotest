from rest_framework.serializers import ModelSerializer
from bookstore.models import Genre, Language, Book, BookInstance, Author


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookInstanceSerializer(ModelSerializer):

    class Meta:
        model = BookInstance
        fields = '__all__'


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
