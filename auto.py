import tweepy, time, pywapi

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


for x in range(1, 99999):
        nowauto = time.strftime("[%I:%M %p] ")
        weather_com_result = pywapi.get_weather_from_weather_com('zipcodehere', units ='imperial') #units can be metric or imperial
        api.update_status(nowauto + "Weather.com: It is currently " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "F in #cityhere.")
        print(nowauto + "Weather.com: It is currently " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "F in #cityhere.")
        time.sleep(900) #time is in seconds
