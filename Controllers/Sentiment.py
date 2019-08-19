import seaborn as sns 

from flask import jsonify 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from Controllers.Cloud_watch import Cloud_watch as cloud_watch

class Sentiment:

    def index():
        data = cloud_watch.index()
        data = data[:40]
        data = Sentiment.anl_tweets(data)
        return jsonify(data)

    def sentiment_analyzer_scores(text, engl=True):
        analyser = SentimentIntensityAnalyzer()

        if engl:
            trans = text
        else:
            trans = translator.translate(text).text
        score = analyser.polarity_scores(trans)
        lb = score['compound']
        if lb >= 0.05:
            return 1
        elif (lb > -0.05) and (lb < 0.05):
            return 0
        else:
            return -1

    def anl_tweets(lst, title='Tweets Sentiment', engl=True ):
        sents = []
        for tw in lst:
            try:
                st = Sentiment.sentiment_analyzer_scores(tw, engl)
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