import tweepy


def getKeyNTokens(doc):
    with open('test.txt', mode='r') as my_file:
        # print(my_file.read())
        Lines = my_file.readlines()
        print(Lines)
        return Lines


# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
