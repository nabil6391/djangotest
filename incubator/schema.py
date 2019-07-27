import graphene
from graphene import Node, Schema, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from incubator.models import App, AppLike, User


class AppType(DjangoObjectType):
    class Meta:
        model = App
        interfaces = (Node,)
        filter_fields = ['id']


class AppLikeType(DjangoObjectType):
    class Meta:
        model = AppLike
        interfaces = (Node,)
        filter_fields = ['app_id', 'uid']


class Query(ObjectType):
    app = Node.Field(AppType)
    all_apps = DjangoFilterConnectionField(AppType)

    like = Node.Field(AppLikeType)
    all_likes = DjangoFilterConnectionField(AppLikeType)


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

        actor_instance = AppLike(app_id=app, uid=user[0])
        actor_instance.save()
        return CreateAppLike(ok=ok, app_like=actor_instance)


class Mutation(ObjectType):
    create_app_like = CreateAppLike.Field()


schema = Schema(query=Query, mutation=Mutation)
