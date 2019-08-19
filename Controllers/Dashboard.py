import tweepy
import json

class Dashboard:

    def index():
        ACCESS_TOKEN = '107282554-vCjzS0Xvdb5h6xnEUYu67mFTUaaUuCPVxCQ2sucd'
        ACCESS_SECRET = 'bt6KXJd6Jfo4qWgoImEZtjiZ7zBk3dF103arwxAUWOljE'
        CONSUMER_KEY = 'u83fQzGVBzGsWbMYEQ3oAwPL1'
        CONSUMER_SECRET = 'rqckM2STaYLQ7RvI3JedImh2tKXeeWzuuzImKObSjAAoApbkkE'
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()

        return Dashboard.coba()

    def coba():
        return 'coba'


        