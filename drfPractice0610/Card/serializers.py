from rest_framework import serializers
from Card.models import Cards


class CardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = ('cardname', 'cardnos', 'validity')
