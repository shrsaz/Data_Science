# -*- coding: utf-8 -*-
"""Twitter Classification using Textblob, Sci-kit learn"""

''' This will make a tuple combination for the tweets and the ID'''

f_modi = open('clean_narendra.txt').read().strip().split('||||||||||')
f_barack = open('clean_barack.txt').read().strip().split('||||||||||')
f_kim = open('clean_kim.txt').read().strip().split('||||||||||')

train = []

for sentence in f_modi:
      train.append(tuple([unicode(sentence.strip(),errors='replace'),'modi']))
''' using unicode function to avoid asci errors while processing the text 
    through NaiveBayesClassifier '''
        
for sentence in f_kim:
      train.append(tuple([unicode(sentence.strip(),errors='replace'),'kim']))
        
for sentence in f_barack:
      train.append(tuple([unicode(sentence.strip(),errors='replace'),'barack']))

        
temp = train
import random
random.shuffle(temp)


from textblob.classifiers import NaiveBayesClassifier
tt=temp[0:500]
cl = NaiveBayesClassifier(tt)
print("done")


#Please enter tweets for testing
cl.classify('India is yearning for a digital revolution, Effort towards #DigitalIndia is all encompassing & aimed at transforming lives')


# # Twitter Classification using Scikit-Learn 

from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC, SVR
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import sent_tokenize, word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.cross_validation import train_test_split
def pre_process(text):
    """
    Function used to process the given text
    1. Replace ,.'" with ''
    2. Tokenzie the text using NLTK word tokenizer
    3. Remove stop words from the token.
    4. Convert the tokens to lower case
    5. Lemmatize the tokens using WordNet Lemmatizer
    :param text: raw review text
    :return: processed tokens
    """
    #print("Hello********************************************************************************************")
    # replace (,.'") with ''
    text = text.replace('||||', '')
    text = text.replace(',', '')
    text = text.replace('@', '')
    text = text.replace('.', '')
    text = text.replace("'", '')
    text = text.replace("\"", '')

     # tokenize into words
    tokens = [word for sent in sent_tokenize(text) for word in word_tokenize(sent)]

    # remove stopwords
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]

    # remove words less than three letters
    tokens = [word for word in tokens if len(word) >= 3]

    # lower capitalization
    tokens = [word.lower() for word in tokens]

    # lemmatize
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]

    return tokens


''' This will make a tuple combination for the tweets and the ID'''
f_modi = open('clean_narendra.txt').read().strip().split('||||||||||')
f_barack = open('clean_barack.txt').read().strip().split('||||||||||')
f_kim = open('clean_kim.txt').read().strip().split('||||||||||')

train = []

for sentence in f_modi:
      train.append(tuple([unicode(sentence.strip(),errors='replace'),'modi']))

for sentence in f_kim:
      train.append(tuple([unicode(sentence.strip(),errors='replace'),'kim']))
        
for sentence in f_barack:
      train.append(tuple([unicode(sentence.strip(),errors='replace'),'barack']))

      
def CalculateSVM(data=None):
    """
    Function is used to classify review text based on Support Vector Machine Classifier
    :param data: Review text with the rating from the data set
    :return: print the accuracy Score
    """
    classifier = LinearSVC()
    vectorizer = TfidfVectorizer(tokenizer=pre_process)
    
    train, test = train_test_split([(t[0],t[1]) for t in data],
                                   test_size=.2,
                                   random_state=10)
    x_train = vectorizer.fit_transform(i[0] for i in train)
    x_test = vectorizer.transform(i[0] for i in test)
    classifier.fit(x_train, [i[1] for i in train])
    score = classifier.score(x_test, [i[1] for i in test])
    #print(classifier.predict(x_train[6]))
    print (score)

    
def CalculateMNB(data=None):
    """
    Function is used to classify review text based on Multinomial Bayes Classifier
    :param data: Review text with the rating from the data set
    :return: print the accuracy Score
    """
    vectorizer = TfidfVectorizer(tokenizer=pre_process)
    classifier = MultinomialNB()
    train, test = train_test_split([(t[0],t[1]) for t in data],
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
    train, test = train_test_split([(t[0],t[1]) for t in data],
                                   test_size=.2,
                                   random_state=10)
    x_train = vectorizer.fit_transform(i[0] for i in train)
    x_test = vectorizer.transform(i[0] for i in test)
    classifier.fit(x_train, [i[1] for i in train])
    score = classifier.score(x_test, [i[1] for i in test])
    print (score)

    
import random
temp=train
random.shuffle(temp)
data=temp[:200]

CalculateSVM(data)
CalculateMNB(data)
CalculateSVR(data)

