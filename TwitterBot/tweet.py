import tweepy


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

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
