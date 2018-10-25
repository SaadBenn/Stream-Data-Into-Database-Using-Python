import mysql.connector
from mysql.connector import Error
import tweepy
import StreamListener


class Connector(object):

    @staticmethod
    def connect(username, created_at, tweet, retweet_count, place, location):
        """
        Streams the data into db

        :param username: column in the database table
        :param created_at: column in the database table
        :param tweet: column in the database table
        :param retweet_count: column in the database table
        :param place: column in the database table
        :param location: column in the database table
        """

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='twitterdb', user='root', password=password, charset='utf8')

            if conn.is_connected():
                """
                Store the data into the db
                """
                cursor = conn.cursor()

                query = "INSERT INTO table (username, created_at, tweet, retweet_count, place, location) VALUES (%s, %s, %s, %s, " \
                        "%s, %s)"
                cursor.execute(query, (username, created_at, tweet, retweet_count, place, location))

                # save changes
                conn.commit()

        except Error as err:
            print(err)

        cursor.close()
        conn.close()


if __name__ == '__main__':
    # access twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    listener = StreamListener(api=api)
    stream = tweepy.Stream(auth, listener=listener)

    track = ['golf', 'masters', 'reed', 'mcilroy', 'woods']
    stream.filter(track=track, languages=['en'])
