from rest_framework import serializers
from User.models import Users


class SnippetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'password', 'username', 'gender', 'language', 'level', 'sendmail')
