# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:14:30 2019

@author: ROG-GL553VD
"""
#Sentiment Analysis Example + Funcition

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

translator = Translator()
analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(text,eng=False):
    if eng:
        text = translator.translate(text).text
    
    score = analyser.polarity_scores(text)
    lb = score['compound']
    if lb >= 0.05:
        return 1
    elif (lb > -0.05) and (lb < 0.05):
        return 0
    else:
        return -1
    
text = 'cuaca disini sangat jelek'
sentiment_analyzer_scores(text,True)