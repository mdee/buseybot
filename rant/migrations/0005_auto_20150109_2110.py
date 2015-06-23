# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def add_busey_clips(apps, schema_editor):
        Clip = apps.get_model('rant', 'Clip')
        clips = [
            {
                'url': 'https://www.youtube.com/watch?v=F73_nmanbVM',
                'desc': 'Busey + hippies + dead chickens',
                'tags': ['chicken', 'hippie', 'rabies', 'suppository', 'feather', 'suit', 'rooster', 'cock', 'stoner', 'stoned', 'insane', 'wtf', 'crazy', 'ridiculous'],
            },
            {
                'url': 'https://www.youtube.com/watch?v=OBBZN7g8W1E',
                'desc': 'Busey & Keanu at a crime scene',
                'tags': ['scream', 'yell', 'argument', 'fight', 'theory', 'argue', 'cop', 'police', 'crime', 'pointbreak', 'reeves', 'keanu', 'patrick', 'swayze', 'point break', 'utah']
            },
            {
                'url': 'https://www.youtube.com/watch?v=kqsN1smBIeE',
                'desc': 'Busey shoots some militants who are shooting birds',
                'tags': ['aim','shoot', 'fire', 'gun', 'season', 'warden', 'hunt', 'bird', 'militant', 'mcbain', 'bulletproof', 'bullet proof','butt', 'horn']
            },
            {
                'url': 'https://www.youtube.com/watch?v=9T2S8GHzxqc',
                'desc': 'Busey jumps in on some coke-peddlers',
                'tags': ['bullet proof', 'sneak','roof','jump','worst','nightmare','coke','cocaine', 'gang', 'crime', 'mcbain', 'bulletproof', 'butt', 'horn']
            },
            {
                'url': 'https://www.youtube.com/watch?v=iQZZHrkBlEI',
                'desc': 'Busey stands firm when the odds are slim',
                'tags': ['caught','trap','relax','calm','gun', 'army', 'military', 'soldier', 'mcbain', 'bullet proof','bulletproof', 'butt', 'horn']
            },
            {
                'url': 'https://www.youtube.com/watch?v=I3nSLhYmS4A',
                'desc': 'Busey is insane in a boat with camo on',
                'tags': ['water','respect','fear','tragedy','loss','afraid','camo','enemy','ridiculous','insane', 'kidnap', 'boat', 'crazy', 'wtf']
            },
            {
                'url': 'https://www.youtube.com/watch?v=GBlfJJ-zYgo',
                'desc': 'Busey is crazy in a diner',
                'tags': ['here', 'gun','ridiclous','mother','mom','diner','afraid','safe','shoot','aim','finish','kill','kitty', 'crazy', 'insane', 'wtf']
            },
            {
                'url': 'https://www.youtube.com/watch?v=hGD3269B0Is',
                'desc': 'Drake Sabitch',
                'tags': ['car','pedestrian','street','walk','run','hit','drake','sabitch','sergeant','sarget','sgt','blacksheep', 'army', 'farley', 'spade', 'black sheep']
            },
            {
                'url': 'https://www.youtube.com/watch?v=F479SR4xeRA',
                'desc': 'Busey shoots that lady by the tree',
                'tags': ['crazy','insane','ridiculous','worry','wife','tree','night','surprise','love', 'lady', 'woman', 'gun', 'wtf']
            },
            {
                'url': 'https://www.youtube.com/watch?v=1tYwDHxg60g',
                'desc': 'Busey and his secretary from "The Firm"',
                'tags': ['desk', 'secretary', 'office', 'tom', 'cruise', 'the firm', 'thefirm', 'firm']
            },
            {
                'url': 'https://www.youtube.com/watch?v=2Ctsm2YRR1g',
                'desc': 'Busey talks with his blind daughter\'s boyfriend',
                'tags': ['dad','date','girlfriend','out','job','blind', 'daughter', 'boyfriend', 'father']
            },
            {
                'url': 'https://www.youtube.com/watch?v=PnSHQHXvaTU',
                'desc': 'Busey is the bad guy in Lethal Weapon',
                'tags': ['triangle','sleeper','hold','punch','attack','wrestle','rain','choke','murtah','riggs','fight', 'gibson', 'lethalweapon', 'mel', 'glover', 'danny', 'lethal weapon']
            },
            {
                'url': 'https://www.youtube.com/watch?v=nrZWG1RWIbQ',
                'desc': 'Busey is a dunk tank clown',
                'tags': ['clown','yell','tank','scary','freaky','insane','scream','harass']
            },
            {
                'url': 'https://www.youtube.com/watch?v=Xm_0VN2T2no',
                'desc': 'Busey and a lighter in Lethal Weapon',
                'tags': ['murtah','riggs','lethalweapon', 'fire', 'lighter', 'gibson', 'mel', 'glover', 'danny', 'lethal weapon']
            },
            {
                'url': 'https://www.youtube.com/watch?v=xLUGdZXET7w',
                'desc': 'Busey is an experiment subject in some lab with a lady',
                'tags': ['chair','lab', 'science', 'experiment']
            },
            {
                'url': 'https://www.youtube.com/watch?v=yEO7Eq6kGiY',
                'desc': 'Busey is being driven by some crazy dude',
                'tags': ['difference','opportunity','chance','cigar','gun','preach','truth','knife','follow','leader','mentor','god','army', 'killer', 'insane', 'crazy', 'wtf']
            },
            {
                'url': 'https://www.youtube.com/watch?v=01X_6koNqBk',
                'desc': 'Busey rolls up on a family and starts being a jerk',
                'tags': ['game face','gameface','mood','burger','rare','kick','punch','trailer','neck','goodbye','squirrel','cage','family','cigar','family', 'park', 'insane', 'crazy', 'wtf','ridiculous']
            },
            {
                'url': 'https://www.youtube.com/watch?v=73yF9rMVjvE',
                'desc': 'Busey in the ship with Steven Seagal',
                'tags': ['cook','chief','superior','mistaken','order','mess','deck','delicious','stew','soup','lard','captain','flavor','officer','strike','striking','fight','punch','meat','locker','seagal', 'ship', 'navy', 'kitchen']
            },
            {
                'url': 'https://www.youtube.com/watch?v=DTcaAhol-lM',
                'desc': 'Busey describes his perfect woman',
                'tags': ['contact','female','utah','surfing','unbelievable','reeves', 'pointbreak', 'lady', 'woman', 'computer', 'reeves', 'keanu', 'patrick', 'swayze', 'point break']
            },
            {
                'url': 'https://www.youtube.com/watch?v=KgWTgXXm4JQ',
                'desc': 'Busey drivin a car and needs to take a leak',
                'tags': ['car', 'drive', 'leak','piss','trip','race','fast']
            },
            {
                'url': 'https://www.youtube.com/watch?v=5-aric34OeE',
                'desc': 'Busey & Ice-T and food and white people',
                'tags': ['manhood','head','best part','flesh','eyes','soul','scar','eye','birth mark','birthmark','dog','blood','lick','bulldog','prince henry stout','prince','chain','fight','kill','turkey','pet','squirrel','love','father','dad','protect','dummy','shotgun','control','emotion','hunt', 'ice-t', 'game', 'pig', 'bulldog', 'dog', 'ice-t', 'ice t', 'cherry bomb']
            },
            {
                'url': 'https://www.youtube.com/watch?v=o1Xdu2HqEtc',
                'desc': 'Busey is Bulletproof',
                'tags': ['shoot','fire','aim','kill','coke','sniff','climb','ladder','arm','trejo','bullet proof','roof','sneak','nightmare','deal','cocaine', 'gun', 'butt', 'mcbain', 'bulletproof', 'butt', 'horn']
            },
            {
                'url': 'https://www.youtube.com/watch?v=ei2dYpiS-Us',
                'desc': 'Busey talking on the phone',
                'tags': ['drop zone','dropzone','tower','electric','power','tank','water','impressed','parachute','plane','flee','kill','sabotage','fall','scar', 'marshall', 'phone', 'boat', 'plane', 'skydive', 'parachute', 'electric', 'murder']
            },
            {
                'url': 'https://www.youtube.com/watch?v=WZppJUaR7_0',
                'desc': 'Busey drops chris farley on the governonr',
                'tags': ['govern','election','patriot','hoist','shoulder','large','american','drop','stuck','crush','chris farley', 'blacksheep', 'black sheep', 'sabitch', 'drake', 'farley']
            },
            {
                'url': 'https://www.youtube.com/watch?v=ZS0YWEC2IO8',
                'desc': 'busey in the kitchen, eye of the tiger',
                'tags': ['predict','uneasy','fear','afraid','vietnam','kitchen','clean','telephone','chat','jb','dirty','prison','gun', 'eye of the tiger', 'eyeofthetiger', 'clean', 'bad feeling', 'vietnam']
            },
            {
                'url': 'https://www.youtube.com/watch?v=803cvniQ1t0',
                'desc': 'Busey doesnt work on Elvis bday',
                'tags': ['eight','8','january','proclaim','dance','king','music','artist','favorite','song','elvis', 'birthday', 'bday', 'work']
            },
            {
                'url': 'https://www.youtube.com/watch?v=uG8apsvGm80',
                'desc': 'wat busey and a kid in wheelchair',
                'tags': ['phillies','philly','baseball','chant','wheelchair','sport', 'yankee', 'indian', 'piss', 'corey haim', 'haim']
            },
            {
                'url': 'https://www.youtube.com/watch?v=5lpR5G2HVek',
                'desc': 'busey is a gay cop',
                'tags': ['yell','angry','mad','commissioner','glove','sadistic','crime scene','scene','case','nephew','gay', 'pussy', 'cop', 'detective', 'murder', 'investigation', 'homosexual', 'queer', 'leather']
            },
            {
                'url': 'https://www.youtube.com/watch?v=iQA4OUkELQI',
                'desc': 'busey clown makeup',
                'tags': ['terrifying','ridiculous','scary','wtf','insane','liquor', 'drunk', 'clown', 'carny', 'mirror', 'makeup', 'make up','lime','fruit','appearance']
            },
            # {
            #     'url': 'https://www.youtube.com/watch?v=y9XSsTnUIMM',
            #     'desc': 'busey tortures mel',
            #     'tags': ['lethal weapon', 'mel', 'gibson', 'mel gibson', 'lethalweapon', 'torture', 'shipment', 'danny', 'glover']
            # },
            {
                'url': 'https://www.youtube.com/watch?v=KkC969nZBw0',
                'desc': 'busey in the old west',
                'tags': ['face','truth','speak','bar','nickel','liar','whore','whip','lie','angry','gun','fire','shoot','rampage','west', 'old', 'lies', 'lyin', 'lie', 'lying', 'frontier', 'saloon', 'bar', 'gamble']
            },
            {
                'url': 'https://www.youtube.com/watch?v=HLCnWtsc6gA',
                'desc': 'busey fucks this guy up in the hospital',
                'tags': ['hospital','doctor','office','medical','revenge','health','anus','jam','fuse','tnt','dynamite','lube','rectum','rectal','suppository', 'eye of the tiger', 'hospital', 'eyeofthetiger', 'ass', 'butt']
            },
            {
                'url': 'https://www.youtube.com/watch?v=p_waSAseRek',
                'desc': 'busey slips on poop',
                'tags': ['drive','angry','car','pet','animal','run','sneak','poop', 'shit', 'dog', 'slip', 'lawn', 'poodle', 'crap', 'turd']
            },
            {
                'url': 'https://www.youtube.com/watch?v=8FnCSJqCWeg',
                'desc': 'busey noises',
                'tags': ['baseball', 'rookie', 'rookieoftheyear', 'rookie of the year']
            },
            {
                'url': 'https://www.youtube.com/watch?v=MznTAWMghqo',
                'desc': '3 minute bulletproof',
                'tags': ['cocaine', 'coke', 'snort', 'trejo', 'butt', 'horn', 'bullet', 'jump', 'rafter', 'roof', 'nightmare', 'mcbain', 'mcbane']
            },
            {
                'url': 'https://www.youtube.com/watch?v=g1D-408WqSM',
                'desc': 'Bulletproof kill count',
                'tags': ['bullet', 'gun', 'fire', 'kill', 'shoot', 'aim', 'pistol', 'mcbain', 'mcbane']
            },
            {
                'url': 'https://www.youtube.com/watch?v=MznTAWMghqo',
                'desc': 'Drake sabitch scares David Spade',
                'tags': ['drake', 'sabitch', 'soldier', 'blacksheep', 'spade', 'farley', 'piss', 'urine', 'black sheep', 'army', 'sargent', 'sergeant', 'donnelly']
            },
            {
                'url': 'https://www.youtube.com/watch?v=hs_l1vorueQ',
                'desc': 'Eye of the TIger clip',
                'tags': ['badass', 'eye of the tiger', 'tiger', 'rampage', 'truck', 'army', 'guns', 'gun', 'drive', 'explosion', 'explode', 'crazy']
            },
            {
                'url': 'https://www.youtube.com/watch?v=MM2jVL-McrY',
                'desc': 'Busey & wheelchair kid',
                'tags': ['card','manager','music','song','baseball','base ball','yankee','phillies','philly','indian','wheelchair','haim','wheel chair','chant','sport']
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
