# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def add_busey_clips(apps, schema_editor):
        Clip = apps.get_model('rant', 'Clip')
        clips = [
            {
                'url': 'https://www.youtube.com/v/F73_nmanbVM?start=30&end=65&autoplay=1',
                'desc': 'Busey + hippies + dead chickens',
                'tags': ['chicken', 'hippie', 'rabies', 'suppository', 'feather'],
            },
            {
                'url': 'https://www.youtube.com/watch?v=OBBZN7g8W1E',
                'desc': 'Busey & Keanu at a crime scene',
                'tags': ['cop', 'police', 'crime', 'pointbreak', 'reeves', 'keanu', 'patrick', 'swayze', 'point break']
            },
            {
                'url': 'https://www.youtube.com/watch?v=kqsN1smBIeE',
                'desc': 'Busey shoots some militants who are shooting birds',
                'tags': ['bird', 'militant', 'mcbain', 'bulletproof', 'butt', 'horn']
            },
            {
                'url': 'https://www.youtube.com/watch?v=9T2S8GHzxqc',
                'desc': 'Busey jumps in on some coke-peddlers',
                'tags': ['cocaine', 'gang', 'crime', 'mcbain', 'bulletproof', 'butt', 'horn']
            },
            {
                'url': 'https://www.youtube.com/watch?v=iQZZHrkBlEI',
                'desc': 'Busey stands firm when the odds are slim',
                'tags': ['gun', 'army', 'military', 'soldier', 'mcbain', 'bulletproof', 'butt', 'horn']
            },
            {
                'url': 'https://www.youtube.com/watch?v=I3nSLhYmS4A',
                'desc': 'Busey is insane in a boat with camo on',
                'tags': ['insane', 'kidnap', 'boat', 'crazy', 'wtf']
            },
            {
                'url': 'https://www.youtube.com/watch?v=GBlfJJ-zYgo',
                'desc': 'Busey is crazy in a diner',
                'tags': ['kitty', 'crazy', 'insane', 'wtf']
            },
            {
                'url': 'https://www.youtube.com/watch?v=hGD3269B0Is',
                'desc': 'Drake Sabitch',
                'tags': ['blacksheep', 'army', 'farley', 'spade', 'black sheep']
            },
            {
                'url': 'https://www.youtube.com/watch?v=F479SR4xeRA',
                'desc': 'Busey shoots that lady by the tree',
                'tags': ['love', 'lady', 'woman', 'gun', 'wtf']
            },
            {
                'url': 'https://www.youtube.com/watch?v=1tYwDHxg60g',
                'desc': 'Busey and his secretary from "The Firm"',
                'tags': ['desk', 'secretary', 'office', 'tom', 'cruise', 'the firm', 'thefirm', 'firm']
            },
            {
                'url': 'https://www.youtube.com/watch?v=2Ctsm2YRR1g',
                'desc': 'Busey talks with his blind daughter\'s boyfriend',
                'tags': ['blind', 'daughter', 'boyfriend', 'father']
            },
            {
                'url': 'https://www.youtube.com/watch?v=PnSHQHXvaTU',
                'desc': 'Busey is the bad guy in Lethal Weapon',
                'tags': ['fight', 'gibson', 'lethalweapon', 'mel', 'glover', 'danny', 'lethal weapon']
            },
            {
                'url': 'https://www.youtube.com/watch?v=nrZWG1RWIbQ',
                'desc': 'Busey is a dunk tank clown',
                'tags': ['clown']
            },
            {
                'url': 'https://www.youtube.com/watch?v=Xm_0VN2T2no',
                'desc': 'Busey and a lighter in Lethal Weapon',
                'tags': ['lethalweapon', 'fire', 'lighter', 'gibson', 'mel', 'glover', 'danny', 'lethal weapon']
            },
            {
                'url': 'https://www.youtube.com/watch?v=xLUGdZXET7w',
                'desc': 'Busey is an experiment subject in some lab with a lady',
                'tags': ['lab', 'science', 'experiment']
            },
            {
                'url': 'https://www.youtube.com/watch?v=yEO7Eq6kGiY',
                'desc': 'Busey is being driven by some crazy dude',
                'tags': ['army', 'killer', 'insane', 'crazy', 'wtf']
            },
            {
                'url': 'https://www.youtube.com/watch?v=01X_6koNqBk',
                'desc': 'Busey rolls up on a family and starts being a jerk',
                'tags': ['family', 'park', 'insane', 'crazy']
            },
            {
                'url': 'https://www.youtube.com/watch?v=73yF9rMVjvE',
                'desc': 'Busey in the ship with Steven Seagal',
                'tags': ['seagal', 'ship', 'navy', 'kitchen']
            },
            {
                'url': 'https://www.youtube.com/watch?v=DTcaAhol-lM',
                'desc': 'Busey describes his perfect woman',
                'tags': ['reeves', 'pointbreak', 'lady', 'woman', 'computer', 'reeves', 'keanu', 'patrick', 'swayze', 'point break']
            },
            {
                'url': 'https://www.youtube.com/watch?v=KgWTgXXm4JQ',
                'desc': 'Busey drivin a car and needs to take a leak',
                'tags': ['car', 'drive', 'leak']
            },
            {
                'url': 'https://www.youtube.com/watch?v=5-aric34OeE',
                'desc': 'Busey & Ice-T and food and white people',
                'tags': ['hunt', 'ice-t', 'game', 'pig']
            },
            {
                'url': 'https://www.youtube.com/watch?v=o1Xdu2HqEtc',
                'desc': 'Busey is Bulletproof',
                'tags': ['cocaine', 'gun', 'butt', 'mcbain', 'bulletproof', 'butt', 'horn']
            }
        ]
        for c in clips:
            clip = Clip(url=c['url'], desc=c['desc'], tags=c['tags'])
            clip.save()

    dependencies = [
        ('rant', '0004_auto_20150109_2051'),
    ]

    operations = [
        migrations.RunPython(add_busey_clips)
    ]
