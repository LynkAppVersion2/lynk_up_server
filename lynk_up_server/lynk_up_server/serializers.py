from rest_framework import serializers
from .models import User, Friend, Group, Event

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('id', 'group_id', 'title', 'date', 'time', 'address')

class UserSerializer(serializers.ModelSerializer):
  events = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ('id', 'user_name', 'phone_number', 'full_name', 'events')

  def get_events(self, obj):
    groups = Group.objects.filter(user=obj)
    events = Event.objects.filter(group__in=groups)
    return EventSerializer(events, many=True).data
