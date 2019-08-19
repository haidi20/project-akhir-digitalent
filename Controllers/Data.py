class data :
	def show_data():
		dt_bukalapak = {"raw": pd.Series(list_tweets(user_id, count, True))}
		tw_bukalapak = pd.DataFrame(dt_bukalapak)
		tw_bukalapak['raw'][3]

		tw_bukalapak['clean_text'] = Data.clean_lst(tw_bukalapak['raw'])
		tw_bukalapak['clean_text'][1]

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

