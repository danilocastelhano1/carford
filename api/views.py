from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models import Person
from api.serializers import PersonSerializer


class PersonViewset(viewsets.ModelViewSet):
    """
    Person viewer, here the magic happens
    added an secure route as the test requires
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]

