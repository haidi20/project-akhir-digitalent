import tweepy
import json

class Dashboard:

    def api():
        ACCESS_TOKEN = '107282554-vCjzS0Xvdb5h6xnEUYu67mFTUaaUuCPVxCQ2sucd'
        ACCESS_SECRET = 'bt6KXJd6Jfo4qWgoImEZtjiZ7zBk3dF103arwxAUWOljE'
        CONSUMER_KEY = 'u83fQzGVBzGsWbMYEQ3oAwPL1'
        CONSUMER_SECRET = 'rqckM2STaYLQ7RvI3JedImh2tKXeeWzuuzImKObSjAAoApbkkE'
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        
        api = tweepy.API(auth)
        public_tweets = api.home_timeline()

        dt_bukalapak = {"raw": pd.Series(list_tweets(user_id, count, True))}
		tw_bukalapak = pd.DataFrame(dt_bukalapak)
		tw_bukalapak['raw'][3]

    def show_data():
		

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


        