
"""Data extraction 
Fetched tweets from Barack Obama, Narendra Modi and Kim kardashian using 
twitter API.The API allows only 200 tweets per ID per API call
As the API allows a max of latest 3200 tweets per ID, so 16 calls for each 
ID were made giving a total of 9,600 tweets
"""

#Code for Narendra Modi

from twython import Twython # pip install twython
import time # standard lib

consumer_key="4dRziGRD3AsKwipyzP9lCcg8n"
consumer_secret="hdeEoacz1v9SLausfAHlhpnWEvsfeqdcAcguS5lTRBrAY9VWc7"

#  Redirected to app's page.
# Create an access token under the the "Your access token" section
access_token="212456898-bJ9dTWM12uF3OUMas4DWEzqsu2NX8lW8fDUZIMVv"
access_token_secret="Ak2GT7jCj5VQgyYPSEtduLFWct0p5hN6OluRJD7K9ALkH"


twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
#lis = [615149853543260160] ## this is the latest starting tweet id

## tweet extract method with the last list item as the max_id
user_timeline = twitter.get_user_timeline(screen_name="narendramodi", count=1)
user_timeline.maxid()

#Output
#615149853543260160

from twython import Twython # pip install twython
import time # standard lib

consumer_key="4dRziGRD3AsKwipyzP9lCcg8n"
consumer_secret="hdeEoacz1v9SLausfAHlhpnWEvsfeqdcAcguS5lTRBrAY9VWc7"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="212456898-bJ9dTWM12uF3OUMas4DWEzqsu2NX8lW8fDUZIMVv"
access_token_secret="Ak2GT7jCj5VQgyYPSEtduLFWct0p5hN6OluRJD7K9ALkH"


twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
#lis = [615149853543260160] ## this is the latest starting tweet id

## tweet extract method with the last list item as the max_id
user_timeline = twitter.get_user_timeline(screen_name="BarackObama", count=1)
user_timeline.maxid()

#Output
#>>617373842839834624 

from twython import Twython # pip install twython
import time # standard lib

consumer_key="4dRziGRD3AsKwipyzP9lCcg8n"
consumer_secret="hdeEoacz1v9SLausfAHlhpnWEvsfeqdcAcguS5lTRBrAY9VWc7"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="212456898-bJ9dTWM12uF3OUMas4DWEzqsu2NX8lW8fDUZIMVv"
access_token_secret="Ak2GT7jCj5VQgyYPSEtduLFWct0p5hN6OluRJD7K9ALkH"


twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
#lis = [615149853543260160] ## this is the latest starting tweet id

## tweet extract method with the last list item as the max_id
user_timeline = twitter.get_user_timeline(screen_name="KimKardashian", count=1)
user_timeline.maxid()

#Output
#>>617149602467201024


# In[ ]:

# Data Scraping

# Fetching text from Twitter for all the individuals using ID

# Code for Narendra Modi and it writes tweet in clean_narendra.txt

# Problem: Initally we were getting just 20 tweets, then 300 per loop(finally 
# after using the code of max iD, finally able to generate 200 tweets per loop)

from twython import Twython # pip install twython
import time # standard lib
consumer_key="4dRziGRD3AsKwipyzP9lCcg8n"
consumer_secret="hdeEoacz1v9SLausfAHlhpnWEvsfeqdcAcguS5lTRBrAY9VWc7"

# Redirected app's page
# Create an access token under the the "Your access token" section
access_token="212456898-bJ9dTWM12uF3OUMas4DWEzqsu2NX8lW8fDUZIMVv"
access_token_secret="Ak2GT7jCj5VQgyYPSEtduLFWct0p5hN6OluRJD7K9ALkH"
filewrite = open('clean_narendra.txt','w')
a=[]
twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
lis = [615149853543260160] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
    print("Printing group :",i)
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="narendramodi",
    count=200, include_retweets=False, max_id=lis[-1])
    #time.sleep(300) ## 5 minute rest between api calls

    for tweet in user_timeline:
        filewrite.write(tweet['text'].encode('utf-8'))
        filewrite.write('||||||||||')
        #print tweet['text'] ## print the tweet
        a.append(tweet['text'])
        lis.append(tweet['id']) ## append tweet id'
        
filewrite.close()


#Code for Barack Obama and it writes tweet in clean_barackobama.txt

from twython import Twython # pip install twython
import time # standard lib
consumer_key="4dRziGRD3AsKwipyzP9lCcg8n"
consumer_secret="hdeEoacz1v9SLausfAHlhpnWEvsfeqdcAcguS5lTRBrAY9VWc7"
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="212456898-bJ9dTWM12uF3OUMas4DWEzqsu2NX8lW8fDUZIMVv"
access_token_secret="Ak2GT7jCj5VQgyYPSEtduLFWct0p5hN6OluRJD7K9ALkH"
filewrite = open('clean_barackobama.txt','w')
a=[]
twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
lis = [617373842839834624] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
    print("Printing group :",i)
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="BarackObama",
    count=200, include_retweets=False, max_id=lis[-1])
    #time.sleep(300) ## 5 minute rest between api calls

    for tweet in user_timeline:
        filewrite.write(tweet['text'].encode('utf-8'))
        filewrite.write('||||||||||')
        #print tweet['text'] ## print the tweet
        a.append(tweet['text'])
        lis.append(tweet['id']) ## append tweet id'
        
filewrite.close()

#Code for Barack Obama to write tweets in clean_Kim.txt

from twython import Twython # pip install twython
import time # standard lib
consumer_key="4dRziGRD3AsKwipyzP9lCcg8n"
consumer_secret="hdeEoacz1v9SLausfAHlhpnWEvsfeqdcAcguS5lTRBrAY9VWc7"
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="212456898-bJ9dTWM12uF3OUMas4DWEzqsu2NX8lW8fDUZIMVv"
access_token_secret="Ak2GT7jCj5VQgyYPSEtduLFWct0p5hN6OluRJD7K9ALkH"
filewrite = open('clean_Kim.txt','w')
a=[]
twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
lis = [617149602467201024] ## this is the latest starting tweet id
for i in range(0, 16): ## iterate through all tweets
    print("Printing group :",i)
## tweet extract method with the last list item as the max_id
    user_timeline = twitter.get_user_timeline(screen_name="KimKardashian",
    count=200, include_retweets=False, max_id=lis[-1])
    #time.sleep(300) ## 5 minute rest between api calls

    for tweet in user_timeline:
        filewrite.write(tweet['text'].encode('utf-8'))
        filewrite.write('||||||||||')
        #print tweet['text'] ## print the tweet
        a.append(tweet['text'])
        lis.append(tweet['id']) ## append tweet id'
        
filewrite.close()


# In[ ]:

#Cleaned the data using code which removes all the RT(retweets)

import numpy
f = open('clean_narendra.txt').read()
new_f=open('clean_narendra.txt','w')

x=[]
y=[]
raw = f.strip().split('||||||||||')
count=0
dataset=[]
for sentence in raw:
    #print(sentence)
    sentencelist = sentence.strip().split()
    if sentencelist and sentencelist[0]!="RT":
        count+=1
        dataset.append(sentence)
        new_f.write(sentence)
        new_f.write('\n')
        new_f.write('||||||||||')
        new_f.write('\n')

#print(count)
#numpy.corrcoef(x,y)
#print(y)


    #type(sentence)
    #print len(sentence.split())
#ptint()
print(count)


import numpy
f = open('clean_barack.txt').read()
new_f=open('clean_barack.txt','w')

x=[]
y=[]
raw = f.strip().split('||||||||||')
count=0
dataset=[]
for sentence in raw:
    #print(sentence)
    sentencelist = sentence.strip().split()
    if sentencelist and sentencelist[0]!="RT":
        count+=1
        dataset.append(sentence)
        new_f.write(sentence)
        new_f.write('\n')
        new_f.write('||||||||||')
        new_f.write('\n')

#print(count)
#numpy.corrcoef(x,y)
#print(y)


    #type(sentence)
    #print len(sentence.split())
#ptint()
print(count)


import numpy
f = open('clean_Kim.txt').read()
new_f=open('clean_Kim.txt','w')

x=[]
y=[]
raw = f.strip().split('||||||||||')
count=0
dataset=[]
for sentence in raw:
    #print(sentence)
    sentencelist = sentence.strip().split()
    if sentencelist and sentencelist[0]!="RT":
        count+=1
        dataset.append(sentence)
        new_f.write(sentence)
        new_f.write('\n')
        new_f.write('||||||||||')
        new_f.write('\n')

#print(count)
#numpy.corrcoef(x,y)
#print(y)


    #type(sentence)
    #print len(sentence.split())
#ptint()
print(count)