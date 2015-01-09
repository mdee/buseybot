# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rant.views import CheckTwitterForBuseyMentionsView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^busey/', CheckTwitterForBuseyMentionsView.as_view())
)
