#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
import hook

@hook.command('cam')
def cam(bot, update):
    which = update.message.text[update.message.text.find(" ")+1:]
    cams = ['hardroom', 'softroom', 'elelab', 'netlab', 'korytarz']
    if which in cams:
        update.message.reply_photo(photo=("http://at.hskrk.pl/dynamic/%s.jpeg?%s" % (which, str(time()))))
    else:
        update.message.reply_text("dunno, available cams: " + ", ".join(cams))
