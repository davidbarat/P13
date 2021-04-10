from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from help.models import Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['date_event', 'group_name','status']