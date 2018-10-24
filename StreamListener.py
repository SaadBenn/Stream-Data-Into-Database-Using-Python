import tweepy


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
