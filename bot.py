import tweepy, time, pywapi

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Make sure access level is Read And Write in the twitter application settings tab
ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

for x in range(1, 99999):
	now = time.strftime("[%I:%M:%S] ")
	weather_com_result = pywapi.get_weather_from_weather_com('zipcodehere', units ='imperial') #units can be imperial or metric
	api.update_status(now + "Weather.com: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "F now in Add City Here. #City")
	print "Weather.com: It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "F now in Add City Here #City."
	time.sleep(900) # time is in seconds
