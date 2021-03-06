# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),

    # URL pattern for user dashboard
    url(
        regex=r'^(?P<username>[\w.@+-]+)/dashboard/$',
        view=views.dashboard,
        name='dashboard'
    ),

    # URL pattern for user page
    url(
        regex=r'^(?P<username>[\w.@+-]+)/page/$',
        view=views.user_page,
        name='userpage'
    ),

    # URL pattern for user dashboard
    url(
        regex=r'^(?P<pk>[\d.@+-]+)/encourage/$',
        view=views.encourage,
        name='encourage'
    ),

    # URL pattern for user dashboard
    url(
        regex=r'^(?P<username>[\w.@+-]+)/encouragements/$',
        view=views.new_encouragements,
        name='new_encouragements'
    ),


]
