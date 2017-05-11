# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.MultipleChoiceQuestionListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<id>[^/]+)/$',
        view=views.MultipleChoiceQuestionDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>[^/]+)/~update/$',
        view=views.MultipleChoiceQuestionUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^answer/(?P<pk>[^/]+)/~update/$',
        view=views.MultipleChoiceAnswerUpdateView.as_view(),
        name='answer-update'
    ),
]
