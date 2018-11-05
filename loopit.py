import tweepy
from time import sleep
from yaml import load
from datetime import datetime

end_date = datetime(2018, 11, 20, 0, 0, 0)
start_counter = 223

credentials = load(open('./credentials.yml'))
CONSUMER_KEY = credentials['database']['CONSUMER_KEY']
CONSUMER_SECRET = credentials['database']['CONSUMER_SECRET']
ACCESS_KEY = credentials['database']['ACCESS_KEY']
ACCESS_SECRET = credentials['database']['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

counter=start_counter
while datetime.now() < end_date:
	counter=counter+1
	api.update_status("Yeah football. Thanks for your service to all the men and women in the military! #SaluteToService /" + str(counter))
	sleep(60)