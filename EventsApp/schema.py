import graphene
import blog.schema
import incubator.schema
import ingredients.schema
import inventory.schema

QUERIES = (
    # Place all future query classes here.
    blog.schema.Query,
    ingredients.schema.Query,
    inventory.schema.Query,
    # bookstore.schema.Query,
    incubator.schema.Query,
    graphene.ObjectType,
)


class Query(*QUERIES):
    """Top level query class that inherits from all others."""
    pass


MUTATIONS = (
    # Place all future Mutation classes here.
    # blog.schema.Mutation,
    # ingredients.schema.Mutation,
    # inventory.schema.Mutation,
    # bookstore.schema.Mutation,
    incubator.schema.Mutation,
    graphene.ObjectType,
)


class Mutation(*MUTATIONS):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


# Mutation for sending the data to the server.
# class Mutation(users.schema.Mutation, events.schema.Mutation, graphene.ObjectType):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()

# Create schema
schema = graphene.Schema(query=Query, mutation=Mutation)
