# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:19:51 2019

@author: ROG-GL553VD
"""
#Reading and analyzing tweets from an id

import tweepy
import re
import seaborn as sns
import numpy as np
import pandas as pd
import json
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS

analyser = SentimentIntensityAnalyzer()
translator = Translator()

ACCESS_TOKEN = '107282554-vCjzS0Xvdb5h6xnEUYu67mFTUaaUuCPVxCQ2sucd'
ACCESS_SECRET = 'bt6KXJd6Jfo4qWgoImEZtjiZ7zBk3dF103arwxAUWOljE'
CONSUMER_KEY = 'u83fQzGVBzGsWbMYEQ3oAwPL1'
CONSUMER_SECRET = 'rqckM2STaYLQ7RvI3JedImh2tKXeeWzuuzImKObSjAAoApbkkE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#create list from tweet
def list_tweets(user_id, count, prt=False):
    tweets = api.user_timeline(
        "@" + user_id, count=count, tweet_mode='extended')
    tw = []
    for t in tweets:
        tw.append(t.full_text)
        if prt:
            print(t.full_text)
            print()
    return tw

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)        
    return input_txt

def _removeNonAscii(s): 
    return "".join(i for i in s if ord(i)<128)

def clean_text(text):
    text = re.sub(r"\n", " ", text)
    # remove ascii
    text = _removeNonAscii(text)
    # to lowecase
    text = text.lower()
    return text

def clean_lst(lst):
    lst_new = []
    for r in lst:
        lst_new.append(clean_text(r))
    return lst_new

def clean_tweets(lst):    
    
    # remove twitter Return handles (RT @xxx:)
    lst = np.vectorize(remove_pattern)(lst, "rt @[\w]*:")
    # remove twitter handles (@xxx)
    lst = np.vectorize(remove_pattern)(lst, "@[\w]*")
    # remove URL links (httpxxx)
    lst = np.vectorize(remove_pattern)(lst, "https?://[A-Za-z0-9./]*")
    # remove punctuation 
    lst = np.core.defchararray.replace(lst, "[^\w\s]+", "")
    # remove special characters, numbers, punctuations (except for #)
    lst = np.core.defchararray.replace(lst, "[^a-zA-Z#]", " ")
    return lst

def sentiment_analyzer_scores(text,eng=False):
    translator = Translator()
    if eng:
        try:
            text = translator.translate(text).text
        except Exception as e:
            print(str(e))
            
    score = analyser.polarity_scores(text)
    lb = score['compound']
    if lb >= 0.05:
        return 1
    elif (lb > -0.05) and (lb < 0.05):
        return 0
    else:
        return -1

def anl_tweets(lst, title='Tweets Sentiment', engl=False ):
    sents = []
    for tw in lst:
        try:
            st = sentiment_analyzer_scores(tw, engl)
            sents.append(st)
        except:
            sents.append(0)
    ax = sns.distplot(
        sents,
        kde=False,
        bins=3)
    ax.set(xlabel='Negative                Neutral                 Positive',
           ylabel='#Tweets',
          title="Tweets of @"+title)
    return sents

user_id = 'jokowi'
count = 200

dt_jokowi = {"raw": pd.Series(list_tweets(user_id, count, True))}
tw_jokowi = pd.DataFrame(dt_jokowi)
tw_jokowi['raw'][3]

tw_jokowi['clean_text'] = clean_lst(tw_jokowi['raw'])
tw_jokowi['clean_text'][1]

tw_jokowi['clean_vector'] = clean_tweets(tw_jokowi['clean_text'])
tw_jokowi['clean_vector'][1]

sentiment_analyzer_scores(tw_jokowi['clean_text'][3],True)

tw_jokowi['sentiment'] = pd.Series(anl_tweets(tw_jokowi['clean_vector'], user_id, True))

#Word Cloud + Sentiment Analysis
stop_words = []
f = open('D:\Documents\Big Data Final (v2) Digitalent\source_code_python\sentiment analysis\data\stopwords.txt', 'r')
for l in f.readlines():
    stop_words.append(l.replace('\n', ''))

f = open('D:\Documents\Big Data Final (v2) Digitalent\source_code_python\sentiment analysis\data\stopwords_indonesia.txt', 'r')
for l in f.readlines():
    stop_words.append(l.replace('\n', ''))
    
additional_stop_words = ['t', 'will']
stop_words += additional_stop_words

def word_cloud(wd_list):
    stopwords = stop_words + list(STOPWORDS)
    all_words = ' '.join([text for text in wd_list])
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        width=1600,
        height=800,
        random_state=21,
        colormap='jet',
        max_words=50,
        max_font_size=200).generate(all_words)
    plt.figure(figsize=(12, 10))
    plt.axis('off')
    plt.imshow(wordcloud, interpolation="bilinear");

word_cloud(tw_jokowi['clean_vector'])
word_cloud(tw_jokowi['clean_vector'][tw_jokowi['sentiment'] == 1])
word_cloud(tw_jokowi['clean_vector'][tw_jokowi['sentiment'] == -1])

user_id = 'aniesbaswedan'
count = 200

dt_aniesbaswedan = {"raw": pd.Series(list_tweets(user_id, count, True))}
tw_aniesbaswedan = pd.DataFrame(dt_aniesbaswedan)
tw_aniesbaswedan['raw'][3]

tw_aniesbaswedan['clean_text'] = pd.Series(clean_lst(tw_aniesbaswedan['raw']))
tw_aniesbaswedan['clean_text'][3]

tw_aniesbaswedan['clean_vector'] = clean_tweets(tw_aniesbaswedan['clean_text'])
tw_aniesbaswedan['clean_vector'][3]

sentiment_analyzer_scores(tw_aniesbaswedan['clean_text'][3],True)

tw_aniesbaswedan['sentiment'] = pd.Series(anl_tweets(tw_aniesbaswedan['clean_vector'], user_id, True))

word_cloud(tw_aniesbaswedan['clean_vector'])
word_cloud(tw_aniesbaswedan['clean_vector'][tw_aniesbaswedan['sentiment'] == 1])
word_cloud(tw_aniesbaswedan['clean_vector'][tw_aniesbaswedan['sentiment'] == -1])