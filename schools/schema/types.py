import graphene

from graphene_django import DjangoObjectType

from users.schema.types import UserType
from schools.models import School, Student, Application



class SchoolType(DjangoObjectType):
    class Meta:
        model = School
        fields = ("id", "name", "address")


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "birth_date", "tutor", "enrollment_date")

    tutor = graphene.Field(UserType)


class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application
        fields = ("id", "student", "school", "application_date", "status")
