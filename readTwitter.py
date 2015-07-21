import json
import io


print "Opening json file ..."
outputFile = 'tweets_710_freeway.json'

# with open("tweets_710_freeway.json") as data_file:    
with open("tweets_710_freeway.json") as data_file:    
    tweets = json.load(data_file)
for tweet in tweets:
    t = tweet['text']
    print t