# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import hashlib
from urllib.parse import urlencode

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from allauth.socialaccount.models import SocialAccount


@python_2_unicode_compatible
class User(AbstractUser):

    STATUS = Choices('1', '2')
    level = StatusField()

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def profile_image_url(self):
        # Set your variables here
        default = None
        size = 100

        fb_uid = SocialAccount.objects.filter(user_id=self.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width={}&height={}".format(fb_uid[0].uid, size, size)

        # construct the url
        gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(self.email.lower().encode('utf-8')).hexdigest() + "?"
        gravatar_url += urlencode({'d': default, 's': str(size)})
        return gravatar_url
