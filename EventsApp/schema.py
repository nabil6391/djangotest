import graphene
import events.schema
import blog.schema
import ingredients.schema
import inventory.schema

QUERIES = (
    # Place all future query classes here.
    blog.schema.Query,
    events.schema.Query,
    ingredients.schema.Query,
    inventory.schema.Query,
    graphene.ObjectType,
)

class Query(*QUERIES):
    """Top level query class that inherits from all others."""
    pass


# Mutation for sending the data to the server.
# class Mutation(users.schema.Mutation, events.schema.Mutation, graphene.ObjectType):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()

# Create schema
schema = graphene.Schema(query=Query)