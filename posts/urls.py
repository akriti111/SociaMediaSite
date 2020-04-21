from django.urls import path,re_path
from .views import (PostList,UserPosts,PostDetail,CreatePost,DeletePost)

app_name = 'posts'

urlpatterns = [

    re_path(r'^$', PostList.as_view(), name='all'),
    re_path(r'new/$', CreatePost.as_view(), name='create'),
    re_path(r'by/(?P<username>[-\w]+)/$', UserPosts.as_view(),name='for_user'),
    re_path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', PostDetail.as_view(), name='single'),
    re_path(r'delete/(?P<pk>\d+)/$', DeletePost.as_view(),name='delete'),

]
