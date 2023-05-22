import pytest
from .factories import UserFactory
from lynk_up_server.models import User, Friend


def test_create_friend(db):
    user1 = UserFactory.create()
    user2 = UserFactory.create()
    user3 = UserFactory.create()

    friendship1 = Friend.objects.create(user=user1, friend=user2)
    friendship2 = Friend.objects.create(user=user1, friend=user3)


    assert friendship1.user == user1
    assert friendship1.friend == user2
    assert friendship2.user == user1
    assert friendship2.friend == user3



    # import ipdb; ipdb.set_trace()
    assert user1.friends() == [user2, user3]
    assert user2.friends() == [user1]
    assert user3.friends() == [user1]

    


