from rest_framework import serializers
from .models import User, Friend, Group, Event

class EventSerializer(serializers.ModelSerializer):
  group_name = serializers.SerializerMethodField()

  class Meta:
    model = Event
    fields = ('id', 'group', 'group_name', 'title', 'date', 'time', 'address', 'description')
  
  def get_group_name(self, obj):
    return obj.group.name

class UserSerializer(serializers.ModelSerializer):
  events = serializers.SerializerMethodField()

  class Meta:
    model = User
    fields = ('id', 'user_name', 'phone_number', 'full_name', 'events')

  def to_representation(self, instance):
    ret = super().to_representation(instance)
    attributes = {'user_name': ret['user_name'], 'phone_number': ret['phone_number'], 'full_name': ret['full_name'], 'events': ret['events']}
    new_representation = {
        'id': ret['id'],
        'type': 'user',
        'attributes': attributes
    }
    return new_representation

  def get_events(self, obj):
    groups = Group.objects.filter(user=obj)
    events = Event.objects.filter(group__in=groups)
    return EventSerializer(events, many=True).data

class GroupSerializer(serializers.ModelSerializer):
  friends = serializers.SerializerMethodField()

  class Meta:
    model = Group
    # fields = '__all__'
    fields = ('id', 'user_id', 'name', 'friends')
  
  def to_representation(self, instance):
    ret = super().to_representation(instance)
    attributes = {'host': ret['user_id'], 'name': ret['name'], 'friends': ret['friends']}

    return{
      'id': ret['id'],
      'type': 'group',
      'attributes': attributes
    }
  
  def get_friends(self, obj):
    friends = obj.friends.all()
    friend_ids = [friend.friend_id for friend in friends]
    users = User.objects.filter(id__in=friend_ids)
    return FriendsListSerializer(users, many=True).data 

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