from django.urls import path,re_path
from .views import (CreateGroup,SingleGroup,ListGroups,JoinGroup,LeaveGroup)

app_name = 'groups'

urlpatterns = [
    re_path(r'^$', ListGroups.as_view(), name='all'),
    re_path(r'^new/$', CreateGroup.as_view(), name='create'),
    re_path(r'posts/in/(?P<slug>[-\w]+)/$', SingleGroup.as_view(), name='single'),
    re_path(r'join/(?P<slug>[-\w]+)/$', JoinGroup.as_view(), name='join'),
    re_path(r'leave/(?P<slug>[-\w]+)/$', LeaveGroup.as_view(), name='leave'),
]
