from rest_framework import serializers
from .models import User, Friend, Group, Event

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ('id', 'group_id', 'title', 'date', 'time', 'address')

class UserSerializer(serializers.ModelSerializer):
  events = serializers.SerializerMethodField()
  # friends = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ('id', 'user_name', 'phone_number', 'full_name', 'events')

  def to_representation(self, instance):
    ret = super().to_representation(instance)
    attributes = {'user_name': ret['user_name'], 'phone_number': ret['phone_number'], 'full_name': ret['full_name']}
    new_representation = {
        'id': ret['id'],
        'attributes': attributes,
        'events': ret['events']
    }
    return new_representation

  def get_events(self, obj):
    groups = Group.objects.filter(user=obj)
    events = Event.objects.filter(group__in=groups)
    return EventSerializer(events, many=True).data

  # def get_friends(self, obj):
  #   return UserSerializer(obj.added_friends(), many=True).data

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = '__all__'

class FriendsListSerializer(serializers.ModelSerializer):
  user_name = serializers.CharField(source='user.user_name')
  user_id = serializers.IntegerField(source='user.id')

  def to_representation(self, instance):
    return {
      'user_name': instance.user_name,
      'user_id': instance.id
    }
  class Meta:
    model = User
    fields = '__all__'
