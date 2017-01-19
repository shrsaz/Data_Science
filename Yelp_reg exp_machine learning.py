# -*- coding: utf-8 -*-
"""

 Scraping the Yelp reviews data for Shake Shake

"""

import requests
import re
''' 
Using only regex to find ratings and reviews from the source pages for Yelp!#
Pages URL follows a particular pattern. for example:
Page 1 URL is : http://www.yelp.com/biz/shake-shack-new-york-9
Page 2 URL is : http://www.yelp.com/biz/shake-shack-new-york-9?start=40
Page 3 URL is : http://www.yelp.com/biz/shake-shack-new-york-9?start=80
We can not guess that url for page n ends with (n-1)*40
i.e url for page 5 should then end with (5-1)*40 => 160.
which is correct: Here's the link to actual url for page 5:-
http://www.yelp.com/biz/shake-shack-new-york-9?start=160
'''
ratings=[] # Creating empty ratings list
reviews=[] # Creating empty reviews list
num_pages = 53
for i in range(1,num_pages): # This for Loops will navigate to each page starting from page 1 and ending at page 52
    if i==1:
        url = 'http://www.yelp.com/biz/shake-shack-new-york-9'   
    else:
        url = "http://www.yelp.com/biz/shake-shack-new-york-9?start="+str((i-1)*40)
    # In the above If statement, for first page, url is the default url for first page. Else use formula to 
    # derive the URL
    
    # request to get the contents of the url
    html = requests.get(url)
    
    
    #  find all the reviews and ratings from this html code
    
    regex_reviews_pattern = '<p itemprop="description" lang="en">(.+?)</p>'
    reg = re.compile(regex_reviews_pattern)  #  compile the pattern 
    match_reviews = re.findall(reg,html.text)
    for t in match_reviews: # for getting a flattened list
        reviews.append(t)
        
    
    # Do similar stuff for ratings.
    
    reg_rating = '<meta itemprop="ratingValue" content=[\S]+'
    regrating=re.compile(reg_rating)
    match_rating = re.findall(regrating,html.text)
    #match rating now have a list of ratings. We will though need to clean this a bit to get the numbers.
   
    for i in range(1,len(match_rating)):# removing the very first number ratings as that corresponds to the overall ratings 
        if match_rating[i]:
            t=re.findall(r'\d',match_rating[i])
            ratings.append(int(t[0]))
    

#result = zip(reviews,ratings)
print("Done")
x=zip(reviews,ratings)


# In[ ]:

# Writing the data into a text file and dividing it using a splitter
f_open=open("yelpdata.txt",'w')
for pair in x:
    st = pair[0]+'||||'+str(pair[1])
    f_open.write(st.encode('utf-8'))
    f_open.write('\n')
    f_open.write("@@@@@@")
    f_open.write('\n')
    
    


# # Yelp Classification using Textblob

# In[50]:

f_yelp = open('yelpdata.txt').read().split('@@@@@@')
data=f_yelp[:1000]

train=[]
for sentence in data:
    temp=sentence.strip().split("||||")
    rev=temp[0]
    rate=int(temp[1])
    train.append(tuple((unicode(rev,errors='replace'),rate)))
    #train.append(tuple([unicode(sentence.strip(),errors='replace'),'modi']))

#train=[(t.strip().split("||||")[0],int(t.strip().split("||||")[1])) for t in data]

temp = train
import random
random.shuffle(temp)
from textblob.classifiers import NaiveBayesClassifier
tt=temp[0:1000]


cl = NaiveBayesClassifier(tt)
print("done")

cl.classify("Burgers are a serious business in the Yelp community and - at least in our community- you will hear the question &#34;what is the best burger ever&#34; a lot. Once you get to talking, with other Yelpers, someone will start praising Shake Shack, guaranteed. So, naturally, when I first heard of it, I had high hopes. <br><br>My first impression was that the menu - like the restaurant - was very crowded and disorganized. The feel of the place is frantic and confused and it doesn&#39;t help the general confusion that they strangely rename common food items so that you have to order &#34;Flat-Top&#34; when you want a hotdog and why they insist on calling a normal cheeseburger a ShackBurger escapes me.")



# # Yelp reviews classification using Scikit-Learn 

f_yelp = open('yelpdata.txt').read().split('@@@@@@')
data=f_yelp[:1000]



def CalculateSVM(data=None):
    """
    Function is used to classify review text based on Support Vector Machine Classifier
    :param data: Review text with the rating from the data set
    :return: print the accuracy Score
    """
    classifier = LinearSVC()
    vectorizer = TfidfVectorizer(tokenizer=pre_process)
    
    train, test = train_test_split([(t.strip().split("||||")[0],int(t.strip().split("||||")[1])) for t in data],
                                   test_size=.2,
                                   random_state=10)
    x_train = vectorizer.fit_transform(i[0] for i in train)
    x_test = vectorizer.transform(i[0] for i in test)
    classifier.fit(x_train, [i[1] for i in train])
    score = classifier.score(x_test, [i[1] for i in test])
    #sent='Had to try this place out since it&#39;s so hyped up. I never had it elsewhere so it was my first time and it as conveniently located down the block of our hotel. There was a long line, but it went by fast so I didn&#39;t have to wait as long as others always complain about. I had the SmokeShack, which was a Cheeseburger topped with all-natural applewood smoked bacon, chopped cherry pepper and ShackSauce. It turned out to be spicy, which was unexpected and also a bit soggy for something that just came fresh out. My boyfriend had the popular Shack Stack which is a Cheeseburger and a crispy mushroom topped with lettuce, tomato and ShackSauce. I gave it a try and did like the texture of the crispy mushroom paired with the burger, but if you&#39;ve been following me, I am not a fan of mushrooms so it was ok to me. The buns were way smaller than the patty, which got a bit messy too. What I did like best about this spot was their crinkled fries! The texture, temperature, and flavor was on point. I would just come back next time just to order the fries. I got the lemonade, which wasn&#39;t anything special, but I definitely want to try the custard milkshake next time I&#39;m back.'
    #i = len(sent.strip().split())
    
    #print(classifier.predict(x_train[0]))
    print (score)


def CalculateMNB(data=None):
    """
    Function is used to classify review text based on Multinomial Bayes Classifier
    :param data: Review text with the rating from the data set
    :return: print the accuracy Score
    """
    vectorizer = TfidfVectorizer(tokenizer=pre_process)
    classifier = MultinomialNB()
    train, test = train_test_split([(t.strip().split("||||")[0],int(t.strip().split("||||")[1])) for t in data],
                                   test_size=.2,
                                   random_state=10)
    x_train = vectorizer.fit_transform(i[0] for i in train)
    x_test = vectorizer.transform(i[0] for i in test)
    classifier.fit(x_train, [i[1] for i in train])
    score = classifier.score(x_test, [i[1] for i in test])
    print (score)

def CalculateSVR(data=None):
    """
    Function is used to classify review text based on Support Vector Regression Classifier
    :param data: Review text with the rating from the data set
    :return: print the accuracy Score
    """
    vectorizer = TfidfVectorizer(tokenizer=pre_process)
    classifier = SVR(kernel='linear')
    train, test = train_test_split([(t.strip().split("||||")[0],int(t.strip().split("||||")[1])) for t in data],
                                   test_size=.2,
                                   random_state=10)
    x_train = vectorizer.fit_transform(i[0] for i in train)
    x_test = vectorizer.transform(i[0] for i in test)
    classifier.fit(x_train, [i[1] for i in train])
    score = classifier.score(x_test, [i[1] for i in test])
    print (score)


CalculateSVM(data)
CalculateSVR(data)
CalculateMNB(data)