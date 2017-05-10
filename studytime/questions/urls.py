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
        regex=r'^~redirect/$',
        view=views.MultipleChoiceQuestionRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<id>[^/]+)/$',
        view=views.MultipleChoiceQuestionDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.MultipleChoiceQuestionUpdateView.as_view(),
        name='update'
    ),
]
