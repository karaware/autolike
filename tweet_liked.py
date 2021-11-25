#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time

CK = 'XXXXX'
CS = 'XXXXX'
AT = 'XXXXX'
AS = 'XXXXX'

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

search_list = ['#家庭菜園', '#プランター菜園', '#ベランダ菜園', '#花', '#TLを花でいっぱいにしよう']
tweet_count = 3

for search in search_list:
    print('Searching... {}' .format(search))
    # サーチ結果 #
    search_result = api.search(q=search, count=tweet_count)
    for tweet in search_result:
        tweet_id = tweet.id
        user = tweet.user.screen_name
        print(user)
        if user != "GTimerapps":
            try:
                # いいねの処理 #
                api.create_favorite(id=tweet_id)
                print('Tweet_liked')
                time.sleep(4)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break



