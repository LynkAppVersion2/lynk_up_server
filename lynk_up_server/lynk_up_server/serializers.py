from rest_framework import serializers
from .models import User, Friend, Group, Event

class EventSerializer(serializers.ModelSerializer):
  group_name = serializers.SerializerMethodField()

  class Meta:
    model = Event
    fields = ('id', 'group', 'group_name', 'title', 'date', 'time', 'address', 'description')
  
  def get_group_name(self, obj):
    return obj.group.name
  
class FriendsListSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = '__all__'

  def to_representation(self, instance):
    return {
      'user_id': instance.id,
      'user_name': instance.user_name,
      'full_name': instance.full_name,
      'phone_number': instance.phone_number
    }
  
  
class GroupsListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = ('id', 'name')

class EventsListSerializer(serializers.ModelSerializer):
  group_name = serializers.SerializerMethodField()

  class Meta:
    model = Event
    fields = ('id', 'group', 'group_name', 'title', 'date', 'time')

  def get_group_name(self, obj):
    return obj.group.name


class GroupSerializer(serializers.ModelSerializer):
  friends_list = serializers.SerializerMethodField()
  events = serializers.SerializerMethodField()

  class Meta:
      model = Group
      fields = ('id', 'user', 'name', 'friends_list', 'events')

  def to_representation(self, instance):
      ret = super().to_representation(instance)
      attributes = {'group_host_id': ret['user'], 'group_name': ret['name'], 'group_friends': ret['friends_list'], 'group_events': ret['events']}

      return {
          'id': ret['id'],
          'type': 'group',
          'attributes': attributes
      }

  def get_friends_list(self, instance):
      friends = instance.friends_list()

      if self.context:
        friends_data = self.initial_data.get('friends_list', [])
        for friend_data in friends_data:
          friend_id = friend_data.get('friend_id')
          friend = Friend.objects.get(friend_id=friend_id)
          instance.friends.add(friend)

      return FriendsListSerializer(friends, many=True, read_only=True).data

  def get_events(self, instance):
      events = instance.events
      return EventsListSerializer(events, many=True, read_only=True).data

class UserSerializer(serializers.ModelSerializer):
  events = EventsListSerializer(many=True)
  groups = GroupsListSerializer(many=True)

  class Meta:
    model = User
    fields = ('id', 'user_name', 'phone_number', 'full_name', 'events', 'groups')

  def to_representation(self, instance):
    ret = super().to_representation(instance)
    attributes = {'user_name': ret['user_name'], 'phone_number': ret['phone_number'], 'full_name': ret['full_name'], 'events': ret['events'], 'groups': ret['groups']}
    new_representation = {
        'id': ret['id'],
        'type': 'user',
        'attributes': attributes
    }
    return new_representation