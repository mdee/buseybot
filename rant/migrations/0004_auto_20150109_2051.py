# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def add_emoji(apps, schema_editor):
        Emoji = apps.get_model('rant', 'Emoji')
        words = [
            'smile',
            'laughing',
            'blush',
            'smiley',
            'relaxed',
            'smirk',
            'heart_eyes',
            'kissing_heart',
            'kissing_closed_eyes',
            'flushed',
            'relieved',
            'satisfied',
            'grin',
            'wink',
            'stuck_out_tongue_winking_eye',
            'stuck_out_tongue_closed_eyes',
            'grinning',
            'kissing',
            'kissing_smiling_eyes',
            'stuck_out_tongue',
            'sleeping',
            'worried',
            'frowning',
            'anguished',
            'open_mouth',
            'grimacing',
            'confused',
            'hushed',
            'expressionless',
            'unamused',
            'sweat_smile',
            'sweat',
            'disappointed_relieved',
            'weary',
            'pensive',
            'disappointed',
            'confounded',
            'fearful',
            'cold_sweat',
            'persevere',
            'cry',
            'sob',
            'joy',
            'astonished',
            'scream',
            'tired_face',
            'angry',
            'rage',
            'triumph',
            'sleepy',
            'yum',
            'mask',
            'sunglasses',
            'dizzy_face',
            'imp',
            'smiling_imp',
            'neutral_face',
            'no_mouth',
            'innocent',
            'alien',
            'heart',
            'broken_heart',
            'fire',
            'poop',
            'thumbsup',
            'thumbsdown',
            'ok_hand',
            'punch',
            'fist',
            'wave',
            'hand',
            'raised_hand',
            'open_hands',
            'point_up',
            'point_down',
            'point_left',
            'point_right',
            'raised_hands',
            'pray',
            'clap',
            'muscle',
            'baby',
            'older_man',
            'man',
            'girl',
            'woman',
            'boy',
            'cop'
        ]
        for w in words:
            emoji = Emoji(word=w)
            emoji.save()


    dependencies = [
        ('rant', '0003_auto_20150109_2033'),
    ]

    operations = [
        migrations.RunPython(add_emoji)
    ]
