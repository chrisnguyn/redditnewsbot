import praw
import tweepy

# Read from file 1 and build Reddit instance
file1 = open("../reddit.txt", "r")
reddit_credentials = file1.read().splitlines()
reddit = praw.Reddit(
    client_id=reddit_credentials[0],
    client_secret=reddit_credentials[1],
    user_agent="mybot"
)
file1.close()


# Read from file 2 and build Twitter client
file2 = open("../twitter.txt", "r")
twitter_credentials = file2.read().splitlines()

API_KEY = twitter_credentials[0]
API_SECRET_KEY = twitter_credentials[1]
ACCESS_TOKEN = twitter_credentials[2]
ACCESS_TOKEN_SECRET = twitter_credentials[3]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# Grab top four posts from the r/worldnews subreddit and print its title and link to the post + tweet them!
posts = reddit.subreddit("worldnews").hot(limit = 4)
for post in posts:
    if (post.stickied == False):
        api.update_status(post.title + " [ https://www.reddit.com" + post.permalink + " ]")
        print(post.title + " [ https://www.reddit.com" + post.permalink + " ]" + "\n")

print("Job done!")