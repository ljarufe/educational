from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model


User = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
