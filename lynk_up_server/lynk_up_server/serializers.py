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
  friends_list = FriendsListSerializer(many=True, required=False)
  events = EventsListSerializer(many=True, read_only=True)

  class Meta:
    model = Group
    fields = ('id', 'user_id', 'name', 'friends_list', 'events')

  def to_representation(self, instance):
    ret = super().to_representation(instance)
    attributes = {'host': ret['user_id'], 'name': ret['name'], 'friends': ret['friends_list'], 'events': ret['events']}

    return{
      'id': ret['id'],
      'type': 'group',
      'attributes': attributes
    }
  

# --------------------------
# LATEST V
# --------------------------
# class GroupSerializer(serializers.ModelSerializer):
#   friends_list = serializers.SerializerMethodField()
#   events = serializers.SerializerMethodField()

#   class Meta:
#       model = Group
#       fields = ('id', 'user', 'name', 'friends_list', 'events')

#   def to_representation(self, instance):
#       import ipdb; ipdb.set_trace()
#       ret = super().to_representation(instance)
#       attributes = {'group_host_id': ret['user'], 'group_name': ret['name'], 'group_friends': ret['friends_list'], 'group_events': ret['events']}

#       return {
#           'id': ret['id'],
#           'type': 'group',
#           'attributes': attributes
#       }

#   def get_friends_list(self, instance):
#       friends = instance.friends.values('friend_id', 'friend__full_name', 'friend__phone_number')
#       modified_friends = []

#       if self.context:
#         friends_data = self.initial_data.get('friends_list', [])
#         for friend_data in friends_data:
#           friend_id = friend_data.get('friend_id')
#           friend = User.objects.get(id=friend_id)
#           modified_friend = {
#             'friend_id': friend_id,
#             'friend_name': friend.full_name,
#             'phone_number': friend.phone_number
#           }
#           modified_friends.append(modified_friend)

#       # if self.data:
#       #   friends_data = self.initial_data.get('friends_list', [])
#       #   for friend_data in friends_data:
#       #       friend_id = friend_data.get('friend_id')
#       #       friend = User.objects.get(id=friend_id)
#       #       modified_friend = {
#       #           'friend_id': friend_id,
#       #           'friend_name': friend.full_name,
#       #           'phone_number': friend.phone_number
#       #       }
#       #       modified_friends.append(modified_friend)

#       for friend in friends:
#         modified_friend = {
#           'friend_id': friend['friend_id'],
#           'friend_name': friend['friend__full_name'],
#           'phone_number': friend['friend__phone_number']
#         }
#         modified_friends.append(modified_friend)
#       return modified_friends

#   def get_events(self, instance):
#       events = instance.events.values('id', 'group_id', 'group__name', 'time', 'title')
#       modified_events = []

#       for event in events:
#         modified_event = {
#           'event_id': event['id'],
#           'group_id': event['group_id'],
#           'group_name': event['group__name'],
#           'title': event['title'],
#           'time': event['time']
#         }
#         modified_events.append(modified_event)
#       return modified_events
# --------------------------
# LATEST ^
# --------------------------

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