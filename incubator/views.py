from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from incubator.serializers import AppSerializer, UserSerializer, AppLikeSerializer, SeerahTopicSerializer, SeerahQuestionSerializer, DictionarySerializer
from incubator.models import App, User, AppLike, SeerahTopic, SeerahQuestion, Dictionary


class AppViewSet(ViewSet):

    def list(self, request):
        queryset = App.objects.order_by('pk')
        serializer = AppSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = App.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AppSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = App.objects.get(pk=pk)
        except App.DoesNotExist:
            return Response(status=404)
        serializer = AppSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = App.objects.get(pk=pk)
        except App.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class UserViewSet(ViewSet):

    def list(self, request):
        queryset = User.objects.order_by('pk')
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AppLikeViewSet(ViewSet):

    def list(self, request):
        queryset = AppLike.objects.order_by('pk')
        serializer = AppLikeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AppLikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = AppLike.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = AppLikeSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = AppLike.objects.get(pk=pk)
        except AppLike.DoesNotExist:
            return Response(status=404)
        serializer = AppLikeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = AppLike.objects.get(pk=pk)
        except AppLike.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SeerahTopicViewSet(ViewSet):

    def list(self, request):
        queryset = SeerahTopic.objects.order_by('pk')
        serializer = SeerahTopicSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SeerahTopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = SeerahTopic.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SeerahTopicSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = SeerahTopic.objects.get(pk=pk)
        except SeerahTopic.DoesNotExist:
            return Response(status=404)
        serializer = SeerahTopicSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = SeerahTopic.objects.get(pk=pk)
        except SeerahTopic.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class SeerahQuestionViewSet(ViewSet):

    def list(self, request):
        queryset = SeerahQuestion.objects.order_by('pk')
        serializer = SeerahQuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SeerahQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = SeerahQuestion.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SeerahQuestionSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = SeerahQuestion.objects.get(pk=pk)
        except SeerahQuestion.DoesNotExist:
            return Response(status=404)
        serializer = SeerahQuestionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = SeerahQuestion.objects.get(pk=pk)
        except SeerahQuestion.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class DictionaryViewSet(ViewSet):

    def list(self, request):
        queryset = Dictionary.objects.order_by('pk')
        serializer = DictionarySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DictionarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Dictionary.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = DictionarySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Dictionary.objects.get(pk=pk)
        except Dictionary.DoesNotExist:
            return Response(status=404)
        serializer = DictionarySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Dictionary.objects.get(pk=pk)
        except Dictionary.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
