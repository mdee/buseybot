# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from os import environ
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from emoji import emojize
import tweepy
from rant.models import BuseyBot


class CheckTwitterForBuseyMentionsView(View):
    """"""
    def get_connection_to_twitter_api(self):
        """"""
        auth = tweepy.OAuthHandler(environ.get('CONSUMER_KEY'), environ.get('CONSUMER_SECRET'))
        auth.set_access_token(environ.get('ACCESS_TOKEN'), environ.get('ACCESS_SECRET'))
        api = tweepy.API(auth)
        return api

    def status_is_retweet(self, status):
        """"""
        return 'retweeted_status' in status._json

    def get(self, request):
        """"""
        api = self.get_connection_to_twitter_api()
        busey_bot = BuseyBot(api_client=api)
        tweets = api.search(q='Gary Busey', count=100, include_entities=False)
        non_retweets = []
        for t in tweets:
            if not self.status_is_retweet(t):
                non_retweets.append(t)
        print 'RT count: {0}'.format(len(tweets) - len(non_retweets))
        busey_bot.reply_to_tweets(non_retweets)
        # for t in good_tweets:
        #     print '{0}\n\t({1}) - {2} - {3}\n'.format(t.text.encode('ascii', 'ignore'), t.id, t.created_at, t.user.screen_name)
        return HttpResponse()

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(CheckTwitterForBuseyMentionsView, self).dispatch(*args, **kwargs)