from rest_framework import serializers
from .models import User, Friend, Group, Event

class EventSerializer(serializers.ModelSerializer):
  group_name = serializers.SerializerMethodField()
  host_id = serializers.SerializerMethodField()
  host_name = serializers.SerializerMethodField()
  invited = serializers.SerializerMethodField()

  class Meta:
    model = Event
    fields = ('id', 'group', 'group_name', 'host_id', 'host_name', 'title', 'date', 'time', 'address', 'description', 'invited')
  
  def get_group_name(self, obj):
    return obj.group.name
  
  def get_host_id(self, obj):
    return obj.group.user.id
  
  def get_host_name(self, obj):
    return obj.group.user.full_name
  
  def get_invited(self, obj):
    friendships = obj.group.friends.all()
    invited_users = friendships.values('friend')
    friends = User.objects.filter(id__in=invited_users)
    return FriendsListSerializer(friends, many=True).data
  

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
  member_count = serializers.SerializerMethodField()

  class Meta:
    model = Group
    fields = ('id', 'name', 'member_count')

  def get_member_count(self, obj):
    return len(obj.friends.all())


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
      attributes = {'group_host_id': ret['user'], 'group_host_name': instance.user.full_name, 'group_name': ret['name'], 'group_friends': ret['friends_list'], 'group_events': ret['events']}

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
          added_friend = Friend.objects.filter(friend_id=friend_id, user_id=instance.user.id)
          accepted_friend = Friend.objects.filter(user_id=friend_id, friend_id=instance.user.id)

          if added_friend.exists():
            for friend in added_friend:
              instance.friends.add(friend)
          if accepted_friend.exists():
            for friend in accepted_friend:
              instance.friends.add(friend)
          # later: if added_friend.exists() and accepted_friend.exists():
            # instance.friends.add(friend)
            # explanation: will only want the ability to add a friend to a group / event if they have accepted the friend request

      return FriendsListSerializer(friends, many=True, read_only=True).data

  def get_events(self, instance):
      events = instance.events
      return EventsListSerializer(events, many=True, read_only=True).data
  

class UserSerializer(serializers.ModelSerializer):
  my_events = EventsListSerializer(many=True)
  invited_to_events = EventsListSerializer(many=True)
  my_groups = GroupsListSerializer(many=True)
  included_in_groups = GroupsListSerializer(many=True)

  class Meta:
    model = User
    fields = ('id', 'user_name', 'phone_number', 'full_name', 'my_events', 'invited_to_events', 'my_groups', 'included_in_groups')

  def to_representation(self, instance):
    ret = super().to_representation(instance)
    attributes = {'user_name': ret['user_name'], 'phone_number': ret['phone_number'], 'full_name': ret['full_name'], 'my_events': ret['my_events'], 'invited_to_events': ret['invited_to_events'], 'my_groups': ret['my_groups'], 'included_in_groups': ret['included_in_groups']}
    new_representation = {
        'id': ret['id'],
        'type': 'user',
        'attributes': attributes
    }
    return new_representation