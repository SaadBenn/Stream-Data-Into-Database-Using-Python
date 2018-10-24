import mysql.connector
from mysql.connector import Error
import tweepy
import json


def connect(username, created_at, tweet, retweet_count, place , location):
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
        conn = mysql.connector.connect(host = 'localhost',
                                       database= 'twitterdb', user='root', password=password, charset='utf8')

        if conn.is_connected():
            """
            Store the data into the db
            """
            cursor = conn.cursor()

            query = "INSERT INTO table (username, created_at, tweet, retweet_count, place, location) VALUES (%s, %s, %s, %s, " \
                    "%s, %s)"
            cursor.execute(query, (username, created_at, tweet, retweet_count, place, location))

            #save changes
            conn.commit()

    except Error as err:
        print(err)

    cursor.close()
    conn.close()



if __name__ == '__main__':


