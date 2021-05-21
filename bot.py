import praw
from prawcore.exceptions import ResponseException
import json

with open('./config.json') as f:
    config = json.load(f)

# Todo Export config in file !!!
reddit = praw.Reddit(
    client_id = config['client_id'],
    client_secret = config['client_secret'],
    username = config['username'],
    password = config['password'],
    user_agent = config['user_agent']
    )

unauthenticated = False

try:
    print(reddit.user.me())
except ResponseException as error:
    print(error)
    unauthenticated = True

if unauthenticated:
    exit()
        
moonshots_subreddit = reddit.subreddit('CryptoMoonShots')

for submissions in moonshots_subreddit.hot(limit = 10):
        print(submissions.title)
