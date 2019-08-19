import re

import pandas as pd

from flask import jsonify 
class Filter:
    def index():
        tweets = pd.read_csv('./sentiment analysis/data/stream_tweet.csv')
        tweets = tweets['text']

        data = []
        for tweet in tweets:
            data.append(Filter.clean_text(tweet))
        
        return jsonify(data)

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
        text = re.sub("com", "", text)
        return text
            
        
