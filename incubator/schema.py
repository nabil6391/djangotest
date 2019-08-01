import graphene
from graphene import Node, Schema, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from incubator.models import App, AppLike, User, SeerahTopic, SeerahQuestion, Dictionary


class AppType(DjangoObjectType):
    class Meta:
        model = App
        interfaces = (Node,)
        filter_fields = ['id']


class AppLikeType(DjangoObjectType):
    class Meta:
        model = AppLike
        interfaces = (Node,)
        filter_fields = ['app', 'user']


class SeerahTopicType(DjangoObjectType):
    class Meta:
        model = SeerahTopic
        interfaces = (Node,)
        filter_fields = ['id', 'name']


class SeerahQuestionType(DjangoObjectType):
    class Meta:
        model = SeerahQuestion
        interfaces = (Node,)
        filter_fields = ['id', 'question','answer']


class DictionaryType(DjangoObjectType):
    class Meta:
        model = Dictionary
        interfaces = (Node,)
        filter_fields = ['word', 'word_diacless','description']



class Query(ObjectType):
    app = Node.Field(AppType)
    all_apps = DjangoFilterConnectionField(AppType)

    like = Node.Field(AppLikeType)
    all_likes = DjangoFilterConnectionField(AppLikeType)

    seerah_question = Node.Field(SeerahQuestionType)
    all_seerah_questions = DjangoFilterConnectionField(SeerahQuestionType)

    seerah_topic = Node.Field(SeerahTopicType)
    all_seerah_topics = DjangoFilterConnectionField(SeerahTopicType)

    dictionary = Node.Field(DictionaryType)
    all_dis = DjangoFilterConnectionField(DictionaryType)






















class CreateAppLike(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        app_id = graphene.Int(required=True)
        uid = graphene.String(required=True)

    # The class attributes define the response of the mutation
    ok = graphene.Boolean()
    app_like = graphene.Field(AppLikeType)

    def mutate(root, info, app_id, uid):
        ok = True

        app = App.objects.get(id=app_id)
        user = User.objects.get_or_create(id=uid)

        actor_instance = AppLike(app=app, user=user[0])
        actor_instance.save()
        return CreateAppLike(ok=ok, app_like=actor_instance)


class Mutation(ObjectType):
    create_app_like = CreateAppLike.Field()


schema = Schema(query=Query, mutation=Mutation)
