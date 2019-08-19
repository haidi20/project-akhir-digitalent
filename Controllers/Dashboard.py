import re
import json
import tweepy
import requests
import pandas as pd
import matplotlib.pyplot as plt

from flask import jsonify, render_template
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from Controllers.Data import Data as data

class Dashboard:

    def index():
        result = data.index()
        # return result
        result = Dashboard.process_wordcloud(result)

        return result

    def process_wordcloud(data):
        # get API key from NewsAPI.org
        NEWS_API_KEY = "498d86e3c11b4142ad84982f58dba794"
        url = "https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey="+NEWS_API_KEY

        # call the api
        response = requests.get(url)

        # get the data in json format
        result = response.json()
        
        # return jsonify(data)

        sentences = ""
        for tweet in data:
            sentences = sentences + " " + tweet
        # return jsonify(sentences)
        # retrun sentence.to_json()

        words = word_tokenize(sentences)
        # return jsonify(words)
        stop_words = set(stopwords.words('english'))

        words = [word for word in words if word not in stop_words and len(word) > 3]

        # now, get the words and their frequency
        words_freq = Counter(words)
        # return jsonify(words_freq)

        words_json = [{'text': word, 'weight': count} for word, count in words_freq.items()]

        # now convert it into a string format and return it
        return json.dumps(words_json)
    


        