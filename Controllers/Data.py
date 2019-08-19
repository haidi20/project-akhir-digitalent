import re

import pandas as pd

from flask import jsonify 
class Data:
    def index():
        tweets = pd.read_csv('./sentiment analysis/data/stream_tweet.csv')
        tweets = tweets['text']

        data = []
        for tweet in tweets:
            data.append(Data.clean_text(tweet))
        
        return data

    def clean_text(text):
        text = text.translate({ord(i): None for i in '@'})
        text = text.translate({ord(i): None for i in '#'})
        text = text.translate({ord(i): None for i in 'RT'})
        text = text.lower()
        text = re.sub(r'\W+', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r"\\", "", text)
        text = re.sub(r"\'", "", text)    
        text = re.sub(r"\"", "", text)
        text = re.sub(r"https", "", text)
        text = re.sub("com", "", text)
        text = re.sub('[^a-zA-Z ?*$!]+', '', text)
        text = re.sub(" \d+", " ", text)
        text = re.sub(r'[0-9]+', '', text)
        return text
            
        