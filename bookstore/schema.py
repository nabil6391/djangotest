from graphene import Node, Schema, ObjectType
from graphene_django import DjangoObjectType, DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField

from bookstore.models import Book,BookInstance

#
# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         interfaces = (Node, )
#         filter_fields = ['name', 'ingredients']
#
#
# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
#         interfaces = (Node, )

#
class Query(ObjectType):
    pass
#     category = Node.Field(CategoryType)
#     all_categories = DjangoFilterConnectionField(CategoryType)
#
#     ingredient = Node.Field(IngredientType)
#     all_ingredients = DjangoConnectionField(IngredientType)

schema = Schema(query=Query)