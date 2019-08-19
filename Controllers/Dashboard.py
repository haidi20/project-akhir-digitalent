import tweepy
import json
import pandas as pd

class Dashboard:
    def index():
        user_id = 'bukalapak'
        count = 200
        
        dt_bukalapak = {"raw": pd.Series(Dashboard.list_tweets(user_id, count, True))}
        tw_bukalapak = pd.DataFrame(dt_bukalapak)
        coba = tw_bukalapak['raw']
        return coba.to_json()

    def api():
        ACCESS_TOKEN = '107282554-vCjzS0Xvdb5h6xnEUYu67mFTUaaUuCPVxCQ2sucd'
        ACCESS_SECRET = 'bt6KXJd6Jfo4qWgoImEZtjiZ7zBk3dF103arwxAUWOljE'
        CONSUMER_KEY = 'u83fQzGVBzGsWbMYEQ3oAwPL1'
        CONSUMER_SECRET = 'rqckM2STaYLQ7RvI3JedImh2tKXeeWzuuzImKObSjAAoApbkkE'
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        
        api = tweepy.API(auth)    
        return api  

    def list_tweets(user_id, count, prt=False):
        tweets = Dashboard.api().user_timeline(
            "@" + user_id, count=count, tweet_mode='extended')
        tw = []
        for t in tweets:
            tw.append(t.full_text)
            if prt:
                print(t.full_text)
                print()
        return tw


        