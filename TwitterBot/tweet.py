import tweepy
import time


def getKeysNTokens(doc):
    with open(doc, mode='r') as my_file:
        # print(my_file.read())
        # Lines = my_file.readlines()
        my_lines = []
        for lines in my_file:
            my_lines.append(lines.strip())

        # print(Lines)
        return my_lines


keys = getKeysNTokens(r'C:\Users\Augus\OneDrive\Desktop\keys.txt')
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        print('I am done')


# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()
#     print(follower.name)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
