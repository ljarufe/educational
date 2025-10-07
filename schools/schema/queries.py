import graphene

from .types import StudentType
from ..models import Student


class SchoolQuery(graphene.ObjectType):
    all_students = graphene.List(StudentType)

    def resolve_all_students(root, info):
        return Student.objects.select_related("tutor").all()
