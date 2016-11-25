import tweepy
import time

consumer_key = 'MmxhEiZav6AL0lD3HJUykEqZu'
consumer_secret = 'YaD1tRxGNlYGlcaNIFFfWN5Zi8PxB53YAhnMIMpA6kqp3uNGUy'
access_key = '800644089943207936-wnoP3JSiTs0mhF0s51rVSwZho5dyw1u'
access_secret = 'g45AbppLZ8xHsELOTYMPjy03Zyrim59O2W5Ktng0Kv2es'


def authorize_account(consumer_key=consumer_key, consumer_secret=consumer_secret,
                      access_key=access_key, access_secret=access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    return tweepy.API(auth)

def read_messages(twitter_account, since = 0):
    mentions = tweepy.Cursor(twitter_account.mentions_timeline, since_id = str(since)).items()
    tweets = []

    for tweet in tweets:
        tweets.append(tweet.text)
        if (tweet.id > since):
            since = tweet.id

    return {"messages": tweets, "since_id": since}


if __name__ == "__main__":

    twitter_account = authorize_account()
    since = 1

    while (True):
        # read all mentions since we last checked
        tweets = read_messages(twitter_account, since)
        since = tweets['since_id']

        # iterate through messages, updating status
        for message in tweets['messages']:
            s = message
            wlist = s.split()
            w1 = list(wlist[0])
            w2 = list(wlist[1])
            b1 = w1[0]
            b2 = w2[0]
            w1[0] = b2
            w2[0] = b1
            message = "".join(w1) + " " + "".join(w2)

            twitter_account.update_status(message)

        # sleep 15 minutes and check again
        time.sleep(60 * 15)