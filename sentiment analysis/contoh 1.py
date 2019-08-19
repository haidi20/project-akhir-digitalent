# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:04:57 2019

@author: ROG-GL553VD
"""
#Sentiment Analysis Example

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
analyser.polarity_scores("The movie is good")
analyser.polarity_scores("The movie is very bad")

#Bobot Sentiment Analysis
def sentiment_analyzer_scores(text):
    score = analyser.polarity_scores(text)
    lb = score['compound']
    if lb >= 0.05:
        return 1
    elif (lb > -0.05) and (lb < 0.05):
        return 0
    else:
        return -1
sentiment_analyzer_scores('The movie is VERY BAD!')
sentiment_analyzer_scores('The movie is long!!!')
sentiment_analyzer_scores('The movie is VERY GOOD!')

#Google Translate
from googletrans import Translator
translator = Translator()
translator.translate('film ini sangat jelek').text

#Google Translate + Sentiment Analysis
text = translator.translate('film ini sangat jelek').text
sentiment_analyzer_scores(text)