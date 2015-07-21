# -*- coding: utf-8 -*- 
#from __future__ import unicode_literals
from bs4 import BeautifulSoup

##########################################################################################################
# This will print out a report showing you how different parsers handle the document, 
# and tell you if you’re missing a parser that Beautiful Soup could be using
#from bs4.diagnose import diagnose
#data = open("710 freeway extension OR project OR tunnel OR corridor lang_en - Twitter Search.html").read()
#diagnose(data)
###########################################################################################################

# Read the html file
filename = '/home/liyang/workspace/pydev_test/710 freeway extension OR project OR tunnel OR corridor lang_en - Twitter Search.html'
f = open(filename, 'r')

# Returned a object of the html file.
soup = BeautifulSoup(f, 'html.parser')

#css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml') # This is for testing


# Extract the time to publish the tweets from the html file.
timeTweets = soup.find_all('small', class_='time')
m= len(timeTweets)
print (m)
count = 0
for timeT in timeTweets:
    if count < 10:
        print  (timeT.a['title'])
        count +=1
    else:
        break
'''     
count = 0
for timeT in timeTweets:
    if count < 10:
        print  (timeT)
        count +=1
    else:
        break
'''    
# Find the tweets from the html file
tweets = soup.find_all('p', class_="TweetTextSize js-tweet-text tweet-text")
n= len(tweets) 
print (n)
count = 0
for tw in tweets:
    if count < 10:
        print  (tw.get_text())#.contents
        count +=1
    else:
        break


f = open('tweet&710','w')
for numTweet in range(n):
        '''temp1 = tweets[numTweet].get_text()
        temp2 = timeTweets[numTweet].a['title']
        temp3 = temp1 + ' ' + temp2 + '\n'
        temp3 = temp3.encode('ascii', 'ignore')'''
        temp = (tweets[numTweet].get_text() + '\n' + timeTweets[numTweet].a['title'] + '\n').encode('ascii', 'ignore')
        print temp
        f.write(temp)
        #f.write(tweets[numTweet].get_text() + timeTweets[numTweet].a['title'])
        #print (tweets[numTweet].get_text()+ u' ' + timeTweets[numTweet].a['title'] + u'\n')
f.close()
       
    #print  (tw['class'])

# The prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string, 
# with each HTML/XML tag on its own line:
# print(soup.prettify())
###########################################

#print(soup.get_text())