# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.MultipleChoiceQuizListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<id>[^/]+)/$',
        view=views.MultipleChoiceQuizDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/~update/$',
        view=views.MultipleChoiceQuizUpdateView.as_view(),
        name='update'
    ),
]
