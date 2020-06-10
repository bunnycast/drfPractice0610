from rest_framework import serializers
from User.models import Users


class UserModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Users
        fields = ('id', 'name', 'password', 'username', 'gender', 'language', 'level', 'sendmail')
