import tweepy, time, pywapi

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text
        reply = status.user.screen_name
        print status.user.screen_name
        weather_com_result = pywapi.get_weather_from_weather_com('zipcodehere', units ='imperial') #can be imperial or metric
        now = time.strftime("[%I:%M %p] ")
        api.update_status(now + "@" + reply + " It is currently " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + "F.", in_reply_to_status_id = status.id)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['@yourbotstwitter'])
