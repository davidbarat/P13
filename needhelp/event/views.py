from django.contrib.auth.models import User
from help.models import Event
from rest_framework import viewsets
from rest_framework import permissions
from event.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]