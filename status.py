import time
import tweepy
import glob
import json

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

fnames = glob.glob("data/*.txt");

#Output file
output = "GeoTweets.txt"

#counter
count = 0

with open(output, 'w') as ofile:
    for fname in fnames:
        print(fname)
        with open(fname, "r") as f:
            for line in f:
                int_list = [int(i) for i in line.split()]
                try:
                    tweet = api.get_status(int_list[0])
                    if tweet.coordinates is not None:
                        ofile.write(str(tweet.user.id) + "\n")
                        ofile.write(tweet.text + "\n")
                        ofile.write(str(tweet.coordinates['coordinates'][0])
                                    + " " + str(tweet.coordinates['coordinates'][1]) + "\n")
                        count += 1
                except tweepy.TweepError as e:
                    if e.api_code == 88:
                        print("Sleep 15min...")
                        print("Total collect: " + str(count))
                        time.sleep(60 * 15)

        print("Total collect: " + str(count))
        print("Finish: " + fname)


