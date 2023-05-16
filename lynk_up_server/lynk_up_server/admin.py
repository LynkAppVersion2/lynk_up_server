from django.contrib import admin
from .models import User
from .models import Friend
from .models import Group
from .models import Event

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Event)