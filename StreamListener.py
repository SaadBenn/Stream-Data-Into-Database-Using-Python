import tweepy
import json
from dateutil import parser
from mysql.connector import Error

from StreamDataIntodb import Connector


class StreamListener(tweepy.StreamListener):
    """
    Tweepy class to access the twitter API
    """

    def on_connect(self):
        print("Connected to the Twitter API")

    def on_error(self, status_code):
        if status_code != 200:
            print("Error")
        else:
            # disconnect the stream
            return False

    def on_data(self, raw_data):

        try:
            raw_data = json.loads(raw_data)

            if 'text' in raw_data:
                username = raw_data['user']['screen_name']
                created_at = parser.parse(raw_data['created_at'])
                tweet = raw_data['text']
                retweet_count = raw_data['retweet_count']

                if raw_data['place'] is not None:
                    place = raw_data['place']['country']
                    print(place)
                else:
                    place = None

                location = raw_data['user']['location']

                Connector.connect(username, created_at, tweet, retweet_count, place, location)
                print("Tweet collected at: {} ".format(str(created_at)))

        except Error as err:
            print(err)
