#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import hook

spaceapi = "http://hskrk-spacemon.herokuapp.com"
def check_anyone():
    request = requests.get(spaceapi)
    if request.status_code == 200:
        data = request.json()
        return data
    else:
        return False

@hook.legacy_command('anyone', 'at')
def anyone(message):
    check = check_anyone()
    if check != False:
        if check['state']['open'] == True:
            if check['sensors']['people_now_present'][0]['value'] > 0:
                return 'Following people are now in HSKRK: %s' % ' '.join(check['sensors']['people_now_present'][0]['names']) 
            else:
                return 'HSKRK is open! 😂'
        else:
            return 'HSKRK is now closed. 😞'
    else:
        return 'cannot connect to spaceapi'
    return
