# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from studytime.questions.views import MultipleChoiceQuestionViewSet, TextQuestionViewSet, TrueOrFalseQuestionViewSet
from studytime.quiz.views import MultipleChoiceQuizViewSet, TextQuizViewSet, TrueOrFalseQuizViewSet
from studytime.scores.views import MultipleChoiceScoreViewSet, TextScoreViewSet, TrueOrFalseScoreViewSet
from studytime.subjects.views import SubjectViewSet

API_TITLE = 'StudyTime API'
API_DESCRIPTION = 'An HTTP API built with Django and Django Rest Framework'

router = routers.SimpleRouter()
router.register(r'textquiz', TextQuizViewSet)
router.register(r'multiplechoicequiz', MultipleChoiceQuizViewSet)
router.register(r'multiplechoicequestion', MultipleChoiceQuestionViewSet)
router.register(r'multiplechoicescore', MultipleChoiceScoreViewSet)
router.register(r'textquiz', TextQuizViewSet)
router.register(r'textquestion', TextQuestionViewSet)
router.register(r'textscore', TextScoreViewSet)
router.register(r'trueorfalsequiz', TrueOrFalseQuizViewSet)
router.register(r'trueorfalsequestion', TrueOrFalseQuestionViewSet)
router.register(r'trueorfalsescore', TrueOrFalseScoreViewSet)
router.register(r'subjects', SubjectViewSet)


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('studytime.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^questions/', include('studytime.questions.urls', namespace='questions')),
    url(r'^quiz/', include('studytime.quiz.urls', namespace='quiz')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^select2/', include('django_select2.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
