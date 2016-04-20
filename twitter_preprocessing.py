#!/usr/bin/env python

import json

LABEL = "homophobic"

tweets = list()

with open('data/stream_faggot.json', 'r') as fr:
    for line in fr.readlines():
        tweet = json.loads(line)
        filtered_tweet = {k: v for k, v in tweet.items() if k == "text"}
        filtered_tweet["label"] = LABEL
        tweets.append(filtered_tweet)

with open('data/filtered_faggot.json', 'w') as fw:
    fw.write(json.dumps(tweets, indent=2))
