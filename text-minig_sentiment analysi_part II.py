# -*- coding: utf-8 -*-
"""
Text mining and sentiment analysis on extracted data.
Removing stop words

"""

# Kim text file and its most common words
import collections
from nltk.corpus import stopwords
freq_counter = collections.Counter()
line = open('clean_kim.txt').read().split('||||||||||')
freq_counter = collections.Counter()
split1 = [sentence.split() for sentence in line]

for sublists in split1:
    for words in sublists:
        if words.lower() not in stopwords.words('english'):
            freq_counter[words]+=1
del freq_counter['&amp;']
freq_counter

# for Barack
line = open('clean_barack.txt').read().split('||||||||||')
freq_counter = collections.Counter()
split1 = [sentence.split() for sentence in line]

for sublists in split1:
    for words in sublists:
        if words.lower() not in stopwords.words('english'):
            freq_counter[words]+=1
del freq_counter['&amp;']
freq_counter

# for modi
line = open('clean_narendra.txt').read().split('||||||||||')
split1 = [sentence.split() for sentence in line]
for sublists in split1:
    for words in sublists:
        if words.lower() not in stopwords.words('english'):
            freq_counter[words]+=1
del freq_counter['&amp;']
freq_counter


"""List o outputs for above 
NarendraModi
Total Output:1739

Kim
Total Output:858

Barack Obama
Total Output:806
"""

"""Sentiment Analysis for all the three personalities """

import numpy
f = open('clean_kim.txt').read()
neg = open('negative-words.txt').read()
neglist = neg.strip().split()
pos = open('positive-words.txt').read()
poslist = pos.strip().split()
global_sentiment=0
x=[]
y=[]
raw = f.strip().split('||||||||||')
for sentence in raw:
    sentencelist = sentence.strip().split()
    xp = 0
    xn = 0
    for word in sentencelist:
        if word in poslist:
            xp+=1
        if word in neglist:
            xn+=1
        sentiment = xp-xn
    y.append(sentiment)
    
    x.append(len(sentencelist))
    print (sentence, (sentiment))
    global_sentiment+=sentiment

#numpy.corrcoef(x,y)
#print(y)

print(global_sentiment)
    #type(sentence)
    #print len(sentence.split())
#print()


# narendra.txt
f = open('clean_narendra.txt').read()
neg = open('negative-words.txt').read()
neglist = neg.strip().split()
pos = open('positive-words.txt').read()
poslist = pos.strip().split()
global_sentiment=0
x=[]
y=[]
raw = f.strip().split('||||||||||')
for sentence in raw:
    sentencelist = sentence.strip().split()
    xp = 0
    xn = 0
    for word in sentencelist:
        if word in poslist:
            xp+=1
        if word in neglist:
            xn+=1
        sentiment = xp-xn
    y.append(sentiment)
    
    x.append(len(sentencelist))
    print (sentence, (sentiment))
    global_sentiment+=sentiment

#numpy.corrcoef(x,y)
#print(y)

print(global_sentiment)
    #type(sentence)
    #print len(sentence.split())
#print()

# barack.text
f = open('clean_barack.txt').read()
neg = open('negative-words.txt').read()
neglist = neg.strip().split()
pos = open('positive-words.txt').read()
poslist = pos.strip().split()
global_sentiment=0
x=[]
y=[]
raw = f.strip().split('||||||||||')
for sentence in raw:
    sentencelist = sentence.strip().split()
    xp = 0
    xn = 0
    for word in sentencelist:
        if word in poslist:
            xp+=1
        if word in neglist:
            xn+=1
        sentiment = xp-xn
    y.append(sentiment)
    
    x.append(len(sentencelist))
    print (sentence, (sentiment))
    global_sentiment+=sentiment

#numpy.corrcoef(x,y)
#print(y)

print(global_sentiment)
    #type(sentence)
    #print len(sentence.split())
#print()




"""Correlation between Length of Sentiment and Tweet of an individual"""

f = open('clean_narendra.txt').read()
neg = open('negative-words.txt').read()
neglist = neg.strip().split()
pos = open('positive-words.txt').read()
poslist = pos.strip().split()
x=[]
y=[]
raw = f.strip().split('||||||||||')
for sentence in raw:
    sentencelist = sentence.strip().split()
    xp = 0
    xn = 0
    for word in sentencelist:
        if word in poslist:
            xp+=1
        if word in neglist:
            xn+=1
        sentiment = xp-xn
    y.append(sentiment)
    
    x.append(len(sentencelist)<5)
    #print (len(sentencelist) , (sentiment))

numpy.corrcoef(x,y)
#print(y)


    #type(sentence)
    #print len(sentence.split())




f = open('clean_narendra.txt').read()
neg = open('negative-words.txt').read()
neglist = neg.strip().split()
pos = open('positive-words.txt').read()
poslist = pos.strip().split()
x=[]
y=[]
raw = f.strip().split('||||||||||')
for sentence in raw:
    sentencelist = sentence.strip().split()
    xp = 0
    xn = 0
    for word in sentencelist:
        if word in poslist:
            xp+=1
        if word in neglist:
            xn+=1
        sentiment = xp-xn
    y.append(sentiment)
    
    x.append(5<len(sentencelist)<10)
    #print (len(sentencelist) , (sentiment))

numpy.corrcoef(x,y)
#print(y)


f = open('clean_Kim.txt').read()
neg = open('negative-words.txt').read()
neglist = neg.strip().split()
pos = open('positive-words.txt').read()
poslist = pos.strip().split()
x=[]
y=[]
raw = f.strip().split('||||||||||')
for sentence in raw:
    sentencelist = sentence.strip().split()
    xp = 0
    xn = 0
    for word in sentencelist:
        if word in poslist:
            xp+=1
        if word in neglist:
            xn+=1
        sentiment = xp-xn
    y.append(sentiment)
    
    x.append(len(sentencelist))
    #print (len(sentencelist) , (sentiment))

numpy.corrcoef(x,y)
#print(y)


#type(sentence)
#print len(sentence.split())


f = open('clean_barack.txt').read()
neg = open('negative-words.txt').read()
neglist = neg.strip().split()
pos = open('positive-words.txt').read()
poslist = pos.strip().split()
x=[]
y=[]
raw = f.strip().split('||||||||||')
for sentence in raw:
    sentencelist = sentence.strip().split()
    xp = 0
    xn = 0
    for word in sentencelist:
        if word in poslist:
            xp+=1
        if word in neglist:
            xn+=1
        sentiment = xp-xn
    y.append(sentiment)
    
    x.append(len(sentencelist))
    #print (len(sentencelist) , (sentiment))

numpy.corrcoef(x,y)
#print(y)


#type(sentence)
#print len(sentence.split())
