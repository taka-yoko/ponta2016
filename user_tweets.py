CONSUMER_KEY = 'ugvKFlivkUGVqgLJgZwYd2gum'
CONSUMER_SECRET_KEY = 'AYKmdB63cNIOtgFL3OCUxNGlvvraaaUZWw6eBS5u5sDtBskz5E'
ACCESS_TOKEN = '838108225-Y7apkNK1Uopxf3e2imJtlUdWzYG2m61YSgbi64ze'
ACCESS_TOKEN_SECRET = '31MFA0GLgVaXQcHsMMvHNWBIPr0FrsGGyMUtzQyfgtyjy'

remain = True
since_id = 718262052746342401
max_id = 782197441969860608
remainNum = 0
count = 200

from twitter import *
from datetime import datetime as dt
import csv
import re

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY))

with open ('ponta.csv', 'w') as f:
  writer = csv.writer(f, lineterminator='\n')
  while remain:
    timelines = t.statuses.user_timeline(screen_name='bs_ponta', count=count, since_id=since_id, max_id=max_id)
    for tweet in timelines:
      if "extended_entities" in tweet:
        userTweets = []
        formated_date = re.sub(r"\d{2}:\d{2}:\d{2}.+$", "", tweet['created_at'])
        userTweets.append(formated_date)
        userTweets.append(re.sub(r"\n", "", tweet['text']))
        userTweets.append(tweet['extended_entities']['media'][0]['media_url'])
        writer.writerow(userTweets)
    if len(timelines) == 0:
      print('finish search')
      remain = False
    else:
      max_id = timelines[-1]['id']-1
      if max_id < since_id:
        print('finish search')
        remain = False