"""SocialMediaSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from .views import (Homepage,TestPage,ThanksPage)

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',Homepage.as_view(),name='home'),
    #path('accounts/',include('accounts.urls',namespace='accounts')),
    #path('accounts/',include('django.contrib.auth.urls')),
    #path('test/',TestPage.as_view(),name='test'),
    #path('thanks/',ThanksPage.as_view(),name='thanks'),
    #path('posts/',include('posts.urls',namespace='posts')),
    #path('groups/',include('groups.urls',namespace='groups')),

    re_path(r'^$', Homepage.as_view(), name='home'),
    re_path(r'^accounts/',include('accounts.urls', namespace='accounts')),
    re_path(r'^accounts/',include('django.contrib.auth.urls')), #This will allows us to connect the authorization things that django has under the hood
    re_path(r'^test/$', TestPage.as_view(), name='test'),
    re_path(r'^thanks/$',ThanksPage.as_view(), name='thanks'),
    re_path(r'^posts/', include('posts.urls', namespace='posts')),
    re_path(r'^groups/', include('groups.urls', namespace='groups')),




]
