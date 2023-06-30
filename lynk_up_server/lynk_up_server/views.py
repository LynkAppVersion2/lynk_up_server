from .models import User, Friend, Group, Event
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods
from operator import attrgetter


@api_view(['GET', 'POST'])
def user_list(request):

  if request.method == 'GET':
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response({"data": serializer.data})
  
  elif request.method == 'POST':
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def user_detail(request, user_id):
  try:
    user = User.objects.get(pk=user_id)
  except User.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = UserSerializer(user)
    return Response({"data": serializer.data})

  elif request.method == 'PATCH':
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

@api_view(['GET', 'POST'])
def group_list(request):
  if request.method == 'GET':
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response({"data": serializer.data})
  
  elif request.method == 'POST':
    serializer = GroupSerializer(data=request.data, context={'request_method': 'PUT'})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'DELETE'])
def group_detail(request, group_id):
  try:
    group = Group.objects.get(pk=group_id)
  except Group.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = GroupSerializer(group)
    return Response({"data": serializer.data})
  
  elif request.method == 'PUT':
    serializer = GroupSerializer(group, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    group.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def event_list(request):
  if request.method == 'GET':
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response({"data": serializer.data})

  if request.method == 'POST':
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, event_id):
  try:
    event = Event.objects.get(pk=event_id)
  except Event.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = EventSerializer(event)
    return Response({"data": serializer.data})

  elif request.method == 'PUT':
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    event.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def friends(request, user_id):
  if request.method == 'GET':
    user = User.objects.get(id=user_id)
    added_friends = user.added_friends()
    accepted_friends = user.accepted_friends()
    all_friends = added_friends + accepted_friends
    sorted_friends = sorted(all_friends, key=attrgetter('full_name'))

    serializer = FriendsListSerializer(sorted_friends, many=True)
    return Response(
      {"data": {"friends":serializer.data}}, status=200, content_type='application/json'
    )

  elif request.method == 'POST':
    try:
      user = User.objects.get(id=user_id)
      friend = User.objects.get(id=request.data['friend'])

      if friend not in user.added_friends():
        Friend.objects.create(user=user, friend=friend)
    except User.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    except IntegrityError:
      return Response(status=status.HTTP_409_CONFLICT)

    serializer = FriendsListSerializer(user.added_friends(), many=True)
    return Response(
      {"data": {"friends":serializer.data}}, status=201, content_type='application/json'
    )


@api_view(['GET', 'DELETE'])
def friend_detail(request, user_id, friend_id):

  if request.method == 'GET':
    user = User.objects.get(id=user_id)
    friend = User.objects.get(id=friend_id)

    serializer = UserSerializer(friend)
    return Response({"data": serializer.data})

  elif request.method == 'DELETE':
    user = User.objects.get(id=user_id)
    friend = User.objects.get(id=friend_id)
    friendship = Friend.objects.filter(user=user, friend=friend).first()
    if friendship:
      friendship.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(status=status.HTTP_404_NOT_FOUND)