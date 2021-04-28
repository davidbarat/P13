# Create your views here.
from help.models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    # group_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = ['date_event', 'group_id', 'group_name', 'status']
        # read_only_fields = ['group_id']
        """
        def create(self, values):
            record = super(Event, self).create(values)
            return record
        """
