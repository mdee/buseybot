# -*- coding: utf-8 -*-
import random
import re

from django.db import models
from picklefield import PickledObjectField


class Clip(models.Model):
    """"""
    url = models.URLField(null=True, blank=True, help_text='Link to a clip of Busey')
    desc = models.CharField(null=True, blank=True, max_length=255, help_text='Briefly describe what happens in this clip')
    tags = PickledObjectField(null=True, blank=True, help_text='A list of words that describe this clip')


class Quotation(models.Model):
    """"""
    text = models.CharField(null=True, blank=True, max_length=255, help_text='Quotations by Gary')


class Emoji(models.Model):
    """"""
    word = models.CharField(null=True, blank=True, max_length=255, help_text='Emojis for tweets')


class Reply(models.Model):
    """"""
    message_id = models.BigIntegerField(null=True, blank=True)


class BuseyBot(object):
    """"""
    def __init__(self, api_client):
        self.clips = Clip.objects.all()
        self.quotations = Quotation.objects.all()
        self.emojis = Emoji.objects.all()
        self.replies = Reply.objects.all()
        self.api_client = api_client
        self.url_length = self.get_configuration_length()
        self.TWEET_LEN = 138 # Doing 138 to leave a space b/w username + URL, & URL + accompanying text
        self.MAX_EMOJIS = 50

    def heads(self):
        """"""
        return random.random() >= 0.5

    def pick_random_number_in_range(self, limit, start=0, limit_inclusive=False):
        """"""
        if not limit_inclusive:
            return random.randrange(start, limit)
        else:
            return random.randint(start, limit)

    def get_configuration_length(self):
        """"""
        twitter_config_data = self.api_client.configuration()
        return twitter_config_data['short_url_length_https']

    def already_replied(self, message_id):
        """"""
        return len(self.replies.filter(message_id=message_id)) > 0

    def tweet_contains_tags(self, tweet_text, tags):
        """"""
        tag_regex = re.compile(r'\(' + r'|'.join(tags) + '\)', re.I)
        return re.search(tag_regex, tweet_text) is not None

    def get_clips_with_tags_that_match_tweet(self, tweet_text):
        """"""
        return [c for c in self.clips if self.tweet_contains_tags(tweet_text, c.tags)]

    def craft_reply(self, status_obj):
        """"""
        username = status_obj.user.screen_name
        # Next step is to pick a clip
        # See if the text of the tweet matches any of the terrible, rudimentary tags that exist
        clips_with_tags = self.get_clips_with_tags_that_match_tweet(status_obj.text)
        if clips_with_tags:
            # Pick one randomly
            reply_clip = clips_with_tags[self.pick_random_number_in_range(limit=len(clips_with_tags))]
        else:
            # No matches, just pick one
            reply_clip = list(self.clips)[self.pick_random_number_in_range(limit=len(self.clips))]
        # Clip is chosen, next step is to decide between emoji or quotation response
        emoji_response = self.heads()
        if emoji_response:
            # Pick a number between 1 and self.MAX_EMOJI, that's the number of emoji you're going to use
            emoji_count = self.pick_random_number_in_range(limit=self.MAX_EMOJIS, limit_inclusive=True)
            # Now, pick random emoji
            reply_text = ''
            emojis_list = list(self.emojis)
            for i in range(emoji_count):
                emoji = emojis_list[self.pick_random_number_in_range(limit=len(emojis_list))]
                reply_text += ':{0}:'.format(emoji.word)
        else:
            # Pick a random quotation to go along with the clip
            quotation = list(self.quotations)[self.pick_random_number_in_range(limit=len(self.quotations))]
            if self.url_length + len(quotation.text) + (len(username) + 1) > self.TWEET_LEN: # +1 for the '@' in the reply
                # The quotation is too long so truncate it
                reply_text = quotation.text[:(self.TWEET_LEN - self.url_length)]
            else:
                reply_text = quotation.text
        # Alright, you've got a clip and a bit of text, time to send it off
        full_reply = '@{0} {1} {2}'.format(username, reply_clip.url, reply_text)
        self.api_client.update_status(full_reply, in_reply_to_status_id=status_obj.id)
        # Finally, save this as a reply
        completed_reply = Reply(message_id=status_obj.id)
        completed_reply.save()

    def reply_to_tweets(self, status_objs):
        """"""
        random.shuffle(status_objs)
        status = None
        for s in status_objs:
            if not self.already_replied(message_id=s.id):
                status = s
                break
        if not status:
            print 'Error! Couldn\'t find a tweet to reply to'
        else:
            self.craft_reply(status)

