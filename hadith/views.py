from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer, BrowsableAPIRenderer, JSONRenderer, AdminRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from hadith.serializers import BookSerializer, ChapterSerializer, CollectionSerializer, HadithSerializer
from hadith.models import Book, Chapter, Collection, Hadith

class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
    def get_default_renderer(self, view):
        return JSONRenderer()

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


class ChapterViewSet(ViewSet):

    def list(self, request):
        queryset = Chapter.objects.order_by('pk')
        serializer = ChapterSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ChapterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Chapter.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ChapterSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Chapter.objects.get(pk=pk)
        except Chapter.DoesNotExist:
            return Response(status=404)
        serializer = ChapterSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Chapter.objects.get(pk=pk)
        except Chapter.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CollectionViewSet(ViewSet):

    def list(self, request):
        queryset = Collection.objects.order_by('pk')
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Collection.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CollectionSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            return Response(status=404)
        serializer = CollectionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class HadithViewSet(ViewSet):

    def list(self, request):
        queryset = Hadith.objects.order_by('pk')
        serializer = HadithSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HadithSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Hadith.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = HadithSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Hadith.objects.get(pk=pk)
        except Hadith.DoesNotExist:
            return Response(status=404)
        serializer = HadithSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Hadith.objects.get(pk=pk)
        except Hadith.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
