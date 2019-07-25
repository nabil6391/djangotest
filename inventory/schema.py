from graphene import Node, Schema, ObjectType
from graphene_django import DjangoObjectType, DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField
from .models import Family, Location, Product, Transaction


class FamilyType(DjangoObjectType):
    class Meta:
        model = Family
        interfaces = (Node,)


class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        interfaces = (Node,)


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        interfaces = (Node,)


class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction
        interfaces = (Node,)


class Query(ObjectType):
    all_families = DjangoConnectionField(FamilyType)
    all_locations = DjangoConnectionField(LocationType)
    all_products = DjangoConnectionField(ProductType)
    all_transactions = DjangoConnectionField(TransactionType)


schema = Schema(query=Query)
