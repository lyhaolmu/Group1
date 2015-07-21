# -*- coding: utf-8 -*-
#! /usr/bin/python

 

# https://dev.twitter.com/docs/using-search

# https://dev.twitter.com/docs/platform-objects/tweets

# https://dev.twitter.com/docs/platform-objects/entities

 
import twitter
import requests, json, time

#from requests_oauthlib import OAuth1

 

#url = 'https://api.twitter.com/1.1/search/tweets.json?q=watch+and+movie&lang=en&count=100&result_type=recent'

#url = 'https://api.twitter.com/1.1/search/tweets.json?q=chevron&lang=en&count=100&result_type=recent'

url = 'https://api.twitter.com/1.1/search/tweets.json?q=710%20freeway%20corridor%20OR%20extension%20OR%20project%20OR%20tunnel%20lang%3Aen&src=typd'

consumer_key = '5dzqHWiCSI0f4qdHjZRedV9oG'

consumer_secret = 'ortFgu8U1HdA6aGrvw2HHdTkquCj33gLdHhmFklCGTzj9pxhfH'

access_token = '3271442413-J3vMaf35leuK2VEYj3dpvUfaRiJyoP0z1yZB4j1'

access_token_secret = 'IHMFumogMELMbKZy5txwjqM3qk2DEX33cmNkpSqu7tnwv'

oauth = twitter.oauth.OAuth(token = access_token, 
                            token_secret = access_token_secret,
                            consumer_key = consumer_key, 
                            consumer_secret = consumer_secret)

#oauth = twitter.oauth2.OAuth2(consumer_key,

#    consumer_secret = consumer_secret,

#    bearer_token = access_token)

    #resource_owner_secret = access_token_secret)

 

since_id = '0'
outputFile = open('Twitters_710Freeway.txt','w')

while True:
    count=0

    try:

        r = requests.get(url + '&since_id=' + since_id, auth = oauth)
        

    except:

        time.sleep(2)

        continue

    if r.status_code != 200:

        time.sleep(20)

        continue

        #raise Exception("Error! status code = " + str(r.status_code))

    data = json.loads(r.text)

    tweets = data['statuses']

    success = 0

    failed = 0


    if len(tweets) > 0:

        for tweet in tweets:

            count+=1

            t = tweet['text']

            id = tweet['id']

            #print(t+'\n')
            
            try:
                outputFile.write(t)
                outputFile.write("\n")
                print(count)
            except ValueError:
                print(count)
                continue
                
            

            #j = json.dumps(tweet)

            #try:

            #    cur.execute(u'INSERT INTO chevron (id,tweet,json) VALUES (%s,%s,%s)', (id, t, j))

            #    success += 1

            #except:

            #    failed += 1

    since_id = data['search_metadata']['max_id_str']

    #print 'succeeded: ' + str(success) + ', failed: ' + str(failed)

    #time.sleep(300)
    time.sleep(20)

 

 

 