# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from .forms import CreateAffirmationForm
from .models import User, Affirmation, Encouragement


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:dashboard',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


@login_required
def dashboard(request, username):
    form = CreateAffirmationForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        messages.success(request, "Affirmation Created")

    affirmations = Affirmation.objects.order_by('-created').all()
    context = {
        "username": request.user.username,
        "affirmations": affirmations,
        "form": form,
    }
    return render(request, "dashboard.html", context)


@login_required
def user_page(request, username):
    user = get_object_or_404(User, username=username)
    affirmations = Affirmation.objects.filter(user=user).all()[:20]
    context = {
        "affirmations": affirmations,
        "username": user.username,
    }
    return render(request, "userpage.html", context)


@login_required
def encourage(request, pk):
    affirmation = get_object_or_404(Affirmation, pk=pk)
    if affirmation.user == request.user:
        return Http404
    Encouragement.objects.get_or_create(encourager=request.user,
                                        affirmation=affirmation)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def new_encouragements(request, username):
    context = {'encour': request.user.new_encouragements}
    if not context['encour']:
        return Http404
    return render(request, "encouragements.html", context)
