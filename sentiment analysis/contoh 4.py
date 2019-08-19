# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 08:20:58 2019

@author: ROG-GL553VD
"""
import tweepy
import time
import re
import seaborn as sns
import numpy as np
import pandas as pd
import csv
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

def twitter_stream_listener(file_name,
                            filter_track,
                            fol=None,
                            loc=None,
                            lang=None,
                            time_limit=20):
    class CustomStreamListener(tweepy.StreamListener):
        def __init__(self, time_limit):
            self.start_time = time.time()
            self.limit = time_limit
            # self.saveFile = open('abcd.json', 'a')
            super(CustomStreamListener, self).__init__()
        def on_status(self, status):
            if (time.time() - self.start_time) < self.limit:
                print(".", end="")
                # Writing status data
                with open(file_name, 'a') as f:
                    writer = csv.writer(f)
#                    print(status)
                    writer.writerow([
                        status.author.screen_name, status.created_at,
                        _removeNonAscii(status.text)
                    ])
            else:
                print("\n\n[INFO] Closing file and ending streaming")
                return False
        def on_error(self, status_code):
            if status_code == 420:
                print('Encountered error code 420. Disconnecting the stream')
                # returning False in on_data disconnects the stream
                return False
            else:
                print('Encountered error with status code: {}'.format(
                    status_code))
                return True  # Don't kill the stream
        def on_timeout(self):
            print('Timeout...')
            return True  # Don't kill the stream
    # Writing csv titles
    print(
        '\n[INFO] Open file: [{}] and starting {} seconds of streaming for {}\n'
        .format(file_name, time_limit, filter_track))
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['author', 'date', 'text'])
    streamingAPI = tweepy.streaming.Stream(
        auth, CustomStreamListener(time_limit=time_limit))
    streamingAPI.filter(
        track=filter_track,
        follow=fol,
        locations=loc,
        languages=lang,
    )
    f.close()

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)        
    return input_txt

def _removeNonAscii(s): 
    return "".join(i for i in s if ord(i)<128)

def clean_text(text):
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"yg", "yang", text)    
    text = re.sub(r"utk", "untuk", text)     
    text = re.sub(r"nya", "", text)
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


#streaming 
filter_track = ['indonesia','jakarta']
file_name = 'data\stream_tweet.csv'
twitter_stream_listener(file_name, filter_track, time_limit=60)

df_tws = pd.read_csv(file_name)
df_tws.shape
df_tws.head

df_tws['clean_text'] = clean_lst(df_tws['text'])
df_tws['clean_vector'] = clean_tweets(df_tws['clean_text'])
df_tws['sentiment'] = pd.Series(anl_tweets(df_tws['clean_vector'], 'indonesia_jakarta', True))

word_cloud(df_tws['clean_vector'])
word_cloud(df_tws['clean_vector'][df_tws['sentiment'] == 1])
word_cloud(df_tws['clean_vector'][df_tws['sentiment'] == -1])