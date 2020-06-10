from rest_framework import viewsets
from User.serializers import UserModelSerializer
from User.models import Users


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = Users.objects.all()
