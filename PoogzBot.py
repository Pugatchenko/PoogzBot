import tweepy
import time

consumer_key = 'zUtTWP49PzX7wAXpziDm8AfKC'
consumer_secret = 'kYSc5wq1bVrj56JF1BLfswX11XpJWhFAdzt7xml1dOhI8ZZEOO'

key = '1291943125250969600-qQxxH6h1bgghQaeqZ7LjwhDefO7hKl'
secret = 'Z7ZZ43qxpZwjibp46gGnx8WANiF8pqiWH08bvtgfbHvy3'

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAO2wGgEAAAAA0ZpJ4jp8QhRQCJgpK1UFgXBt0c8%3Db5qAWixe0f8JzWHtzVVDhSypRALsAYmh54Xjv3Xc9qHKVWw4iT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if "pootie" in tweet.full_text.lower():
            print(str(tweet.id) + " - " + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " auto-reply, like, and retweet works :)", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(2)