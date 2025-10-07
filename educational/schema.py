import graphene

from schools.schema import SchoolQuery

class Query(
    SchoolQuery,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)
