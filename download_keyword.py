#test
import twitter
import json
import io
import urlparse
from numpy import result_type

def oauth_login():
    
    CONSUMER_KEY = '5dzqHWiCSI0f4qdHjZRedV9oG'
    CONSUMER_SECRET = 'ortFgu8U1HdA6aGrvw2HHdTkquCj33gLdHhmFklCGTzj9pxhfH'
    OAUTH_TOKEN = '3271442413-J3vMaf35leuK2VEYj3dpvUfaRiJyoP0z1yZB4j1'
    OAUTH_TOKEN_SECRET = 'IHMFumogMELMbKZy5txwjqM3qk2DEX33cmNkpSqu7tnwv'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def twitter_search(twitter_api, q, max_results=1000, **kw):
 
    #search_results = twitter_api.search.tweets(q=q, count=100, **kw)
    #search_results = twitter_api.search.tweets(q=q, count=15, result_type='*recent', until = '2015-07-01', **kw)
    search_results = twitter_api.search.tweets(q=q, count=100, since_id=100,  **kw)
    
    statuses = search_results['statuses']

    max_results = min(1000, max_results)
    tweet_count = 0

    for _ in range(10):
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError, e: 
            break
            
        kwargs = dict([ kv.split('=') 
                        for kv in next_results[1:].split("&") ])
        # next_results = urlparse.parse_qsl(next_results[1:])
        # kwargs = dict(next_results)

        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        
        tweet_count += 100
        print tweet_count
        
        if len(statuses) > max_results: 
            break
            
    return statuses

twitter_api = oauth_login()
print "Authed to Twitter. Searching now........"

q = "FasTrak" 
#"710+freeway"
#q = "710%20freeway%20corridor%20OR%20tunnel%20OR%20extension%20OR%20project"
#"710%20freeway" #91
# "710+freeway+corridor+OR+extension+OR+project+OR+tunnel" #3 entry"710+freeway"
tweets = twitter_search(twitter_api, q, max_results=1000)

print "Results retrieved ..."
t_710Freeway=[]
if len(tweets) > 0:
    count = 0
    for tweet in tweets:
        t_710Freeway.append((tweet['text'],tweet['id']))
        count += 1
        t = tweet['text']
        print t

print "Saving to json file ..."
outputFile = open('tweets_FasTrak.json','w')
json.dump(tweets, outputFile)
outputFile.close()

print len(t_710Freeway)
for i in t_710Freeway:
    print i
