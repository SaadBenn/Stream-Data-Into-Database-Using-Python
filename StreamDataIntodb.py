#!usr/bin/python

import mysql.connector
from mysql.connector import Error
import tweepy
import json
import os
import subprocess

def test():
    subprocess.call('./settings.sh', shell=True)

    consumer_key = os.environ(['CONSUMER_KEY'])
    consumer_secret = os.environ(['CONSUMER_SECRET'])
    access_token = os.environ(['ACCESS_TOKEN'])
    access_token_secret = os.environ(['ACCESS_TOKEN_SECRET'])
    password = os.environ(['PASSWORD'])


if __name__ == '__main__':
    test()
