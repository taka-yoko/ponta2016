CONSUMER_KEY = 'ugvKFlivkUGVqgLJgZwYd2gum'
CONSUMER_SECRET_KEY = 'AYKmdB63cNIOtgFL3OCUxNGlvvraaaUZWw6eBS5u5sDtBskz5E'
ACCESS_TOKEN = '838108225-Y7apkNK1Uopxf3e2imJtlUdWzYG2m61YSgbi64ze'
ACCESS_TOKEN_SECRET = '31MFA0GLgVaXQcHsMMvHNWBIPr0FrsGGyMUtzQyfgtyjy'

from twitter import *

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY))

timelines = t.statuses.home_timeline()

for timelime in timelines:
  tl = '({id})[{username}]:{text}'.format(id=timelime['id'], username=timelime['user']['name'], text=timelime['text'])
  print(tl)