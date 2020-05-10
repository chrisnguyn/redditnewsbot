import praw

file = open("../info.txt", "r")
credentials = file.read().splitlines()

reddit = praw.Reddit(
    client_id=credentials[0],
    client_secret=credentials[1],
    user_agent="mybot"
)

file.close()

posts = reddit.subreddit("worldnews").hot(limit = 5)

for post in posts:
    if (post.stickied == False):
        print(post.title + " [ https://www.reddit.com" + post.permalink + " ]" + "\n")