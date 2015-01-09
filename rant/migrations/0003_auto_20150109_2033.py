# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def add_busey_quotes(apps, schema_editor):
        """"""
        Quotation = apps.get_model('rant', 'Quotation')
        quotes = [
            'My dark side, my shadow, my lower companion is now in the back room blowing up balloons for kids\' parties.',
            'I love love, and I love life. I love. I just love. It\'s just great. It\'s the most enduring element we have is love.',
            'You know what \'DOUBT\' stands for? It stands for \'Debate On Understanding Bewildersome Thoughts.\'',
            'You know what \'FAILING\' stands for? It stands for \'Finding An Important Lesson, Inviting Needed Growth.\'',
            'I\'m not jealous, and I\'m not possessive, and I\'m not controlling.',
            'Nothing changes like changes, because nothing changes but the changes.',
            'I\'ve been told by doctors and surgeons that I have the energy of ten men who have normal jobs.',
            'It\'s a very strange silence that I\'m living in right now. It\'s a silence that has a lot of activity and noise in it from a zone that I don\'t live in on this earth.',
            "Winners do what losers don't want to do.",
            "Imagine the peace symbol. The peace symbol has three pieces in it. One piece is emotion, that's your body. Another piece has spirit in it, that's your fuel. Another piece has intellect in it and that's your steering wheel. You can never overdo the fuel that goes into the body, which is the emotions and the steering wheel to drive it.",
            "It's good for everyone to understand that they are to love their enemies, simply because your enemies show you things about yourself you need to change. So in actuality enemies are friends in reverse.",
            "Have a mind that's open to everything, get attached to nothing.",
            "Fear is the dark room where the Devil develops his negatives.",
            "Amen is not the end of a prayer, it just gets us ready to go to the next level.",
            "I don't know where I come from but I'm here now so deal with it.",
            "If you take shortcuts, you get cut short.",
            "There has got to be more to life than being a really, really, ridiculously good actor.",
            "I'll tell you this: You have to remember to chase and catch your dreams, because if you don't, your imagination will live in empty spaces, and that's nowhere land.",
            "Never dip lower than you can dip.",
            "I'm interested in all things that Donald Trump does. I've known him since 1980. He's a good man.",
            "I consider myself a Texan. I grew up in Texas and Oklahoma.",
            "I don't know how I got involved in 'Celebrity Wife Swap.' It came from my agent Hugh. He got the opportunity for me."
        ]
        for q in quotes:
            if len(q) <= 255:
                quote = Quotation(text=q)
                quote.save()

    dependencies = [
        ('rant', '0002_auto_20150109_2033'),
    ]

    operations = [
        migrations.RunPython(add_busey_quotes)
    ]
