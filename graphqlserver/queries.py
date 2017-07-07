from graphql import GraphQLObjectType, GraphQLField, GraphQLString


class QueryMeta(type):
    """
    Validates and registers a query.

    TODO: Register the query in a metaclass
    """
    pass


class Query(metaclass=QueryMeta):
    """
    Base class for GraphQL queries.
    """
    def as_graphql(self):
        field = GraphQLField(type=GraphQLString, resolver=self.get_queryset)
        return GraphQLObjectType(name='RootQueryType', fields={'hello': field})
