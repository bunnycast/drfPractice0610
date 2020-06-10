from rest_framework import viewsets
from Card.serializers import CardModelSerializer
from Card.models import Cards


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardModelSerializer
    queryset = Cards.objects.all()
