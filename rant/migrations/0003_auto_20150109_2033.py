# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def add_busey_quotes(apps, schema_editor):
        """"""
        Quotation = apps.get_model('rant', 'Quotation')
        quotes = [
            'When a loved one is in pain, I am the one in agony.',
            'I don’t know where I come from but I’m here now so deal with it.',
            'I\'m not jealous, and I\'m not possessive, and I\'m not controlling.',
            'Nothing changes like changes, because nothing changes but the changes.',
            'I\'ve been told by doctors and surgeons that I have the energy of ten men who have normal jobs.',
            'The sun setting over the ocean makes an exclamation mark in reverse.',
            "Winners do what losers don't want to do.",
            "You can have a very robust conversation with coffee.",
            "Your imagination is the hood ornament on the car of your creativity.",
            "Have a mind that's open to everything, get attached to nothing.",
            "Fear is the dark room where the Devil develops his negatives.",
            "Amen is not the end of a prayer, it just gets us ready to go to the next level.",
            "I don't know where I come from but I'm here now so deal with it.",
            "When you get lost in your imaginatory vagueness your foresight will become a nimble vagrant.",
            "If you take shortcuts, you get cut short.",
            "There has got to be more to life than being a really, really, ridiculously good actor.",
            "Great things like this only happen for the first time once.",
            "Never dip lower than you can dip.",
            "I consider myself a Texan. I grew up in Texas and Oklahoma.",
            "Men are failed women at birth.",
            "The most controversial thing I've ever done... is nothing.",
            "Never dip lower than you can dip.",
            "'GAY' stands for 'Good As You'.",
            "I can hear my toenails grow.",
            "'DEATH' means 'Don't Expect A Tragedy Here'"
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
