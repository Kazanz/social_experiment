# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    control = models.NullBooleanField(null=True)
    login_count = models.IntegerField(default=0)
    recent_login = models.DateTimeField(null=True)
    dummy_user = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def save(self, *args, **kwargs):
        if self.control is None and not self.dummy_user:
            self.control = User.control_count() < User.experiment_count()
        return super(User, self).save(*args, **kwargs)

    @staticmethod
    def control_count():
        return User.objects.filter(control=True).count()

    @staticmethod
    def experiment_count():
        return User.objects.filter(control=False).count()

    @property
    def new_encouragements(self):
        affirmations = Affirmation.objects.filter(user=self).all()
        logins = Login.objects.order_by('-pk').filter(user=self).all()
        if len(logins) < 2:
            return []
        return Encouragement.objects.filter(
            created__gte=logins[1].time,
            affirmation__in=affirmations
        ).all()


class Affirmation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    @property
    def likes(self):
        return Encouragement.objects.filter(affirmation=self).count()

    @property
    def encouragers(self):
        encouragements = Encouragement.objects.filter(affirmation=self).all()
        usernames = [e.encourager.username for e in encouragements]
        html = ['<p><a href="/users/{0}/page/">{0}</a></p>'.format(username)
                for username in usernames]
        return " ".join(html)


class Encouragement(models.Model):
    encourager = models.ForeignKey(settings.AUTH_USER_MODEL)
    affirmation = models.ForeignKey(Affirmation)
    created = models.DateTimeField(auto_now=True)


class Login(models.Model):
    time = models.DateTimeField()
    user = models.ForeignKey(User)


def track(sender, user, request, **kwargs):
    user.login_count += 1
    user.save()
    Login.objects.create(user=user, time=now())


user_logged_in.connect(track)
