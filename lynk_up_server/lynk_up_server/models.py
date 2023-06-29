from django.db import models

class User(models.Model):
  user_name = models.CharField(max_length=20, unique=True, blank=True)
  phone_number = models.CharField(max_length=12, unique=True)
  full_name = models.CharField(max_length=40)

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user_name

  def added_friends(self):
    return [friend.friend for friend in Friend.objects.filter(user=self)]

  def accepted_friends(self):
    return [friend.user for friend in Friend.objects.filter(friend=self)]
  
  def my_groups(self):
    return self.groups.all()

  def included_in_groups(self):
      return Group.objects.filter(
          friends__friend_id__in=Friend.objects.filter(friend=self).values('friend_id')
      )

  def my_events(self):
      return Event.objects.filter(group__in=self.my_groups())

  def invited_to_events(self):
      return Event.objects.filter(group__in=self.included_in_groups())
  

class Friend(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Friendship between {self.user} and {self.friend}"


class Group(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups')
  friends = models.ManyToManyField(Friend, blank=True)
  name = models.CharField(max_length=40)

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  
  def friends_list(self):
    return User.objects.filter(id__in=self.friends.values('friend_id'))

class Event(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='events')
  title = models.CharField(max_length=40)
  date = models.CharField(max_length=50)
  time = models.CharField(max_length=40)
  address = models.CharField(max_length=60)
  description = models.CharField(max_length=200)

  updated = models.DateTimeField(auto_now=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
