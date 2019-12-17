#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import hook

def getBodyPart(part):
    request = requests.get("http://api.o{}.ru/{}/0/1/random".format(part, part))
    data = request.json()
    url = 'http://media.o{}.ru/{}/{}.jpg'.format(part, part, str(data[0]['id']).zfill(5))
    test = requests.get(url)
    if test.status_code == 200:
        return url
    else:
        return False

def fetchBodyPart(part):
    retry_count = 3
    while retry_count > 0:
        parts = getBodyPart(part)
        if parts:
            return parts
        retry_count -= 1
    return None

@hook.command('boobs')
def oboobs(bot, update):
    part = fetchBodyPart('boobs')
    if not part:
        update.message.reply_text('found no boobs for you')
    else:
        update.message.reply_photo(photo=part)

@hook.command('butts')
def obutts(bot, update):
    part = fetchBodyPart('butts')
    if not part:
        update.message.reply_text('found no butt for you')
    else:
        update.message.reply_photo(photo=part)
