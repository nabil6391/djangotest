from rest_framework.serializers import ModelSerializer
from incubator.models import App, User, AppLike, SeerahTopic, SeerahQuestion, Dictionary


class AppSerializer(ModelSerializer):

    class Meta:
        model = App
        fields = '__all__'


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class AppLikeSerializer(ModelSerializer):

    class Meta:
        model = AppLike
        fields = '__all__'


class SeerahTopicSerializer(ModelSerializer):

    class Meta:
        model = SeerahTopic
        fields = '__all__'


class SeerahQuestionSerializer(ModelSerializer):

    class Meta:
        model = SeerahQuestion
        fields = '__all__'


class DictionarySerializer(ModelSerializer):

    class Meta:
        model = Dictionary
        fields = '__all__'
