from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from bookstore.serializers import GenreSerializer, LanguageSerializer, BookSerializer, BookInstanceSerializer, AuthorSerializer
from bookstore.models import Genre, Language, Book, BookInstance, Author


class GenreViewSet(ViewSet):

    def list(self, request):
        queryset = Genre.objects.order_by('pk')
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Genre.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = GenreSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=404)
        serializer = GenreSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LanguageViewSet(ViewSet):

    def list(self, request):
        queryset = Language.objects.order_by('pk')
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Language.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = LanguageSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            return Response(status=404)
        serializer = LanguageSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BookViewSet(ViewSet):

    def list(self, request):
        queryset = Book.objects.order_by('pk')
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=404)
        serializer = BookSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class BookInstanceViewSet(ViewSet):

    def list(self, request):
        queryset = BookInstance.objects.order_by('pk')
        serializer = BookInstanceSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookInstanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = BookInstance.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = BookInstanceSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = BookInstance.objects.get(pk=pk)
        except BookInstance.DoesNotExist:
            return Response(status=404)
        serializer = BookInstanceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = BookInstance.objects.get(pk=pk)
        except BookInstance.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AuthorViewSet(ViewSet):

    def list(self, request):
        queryset = Author.objects.order_by('pk')
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=404)
        serializer = AuthorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
