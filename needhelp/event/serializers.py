# Create your views here.
from help.models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = ['date_event', 'group_id', 'group_name', 'status']
