import praw
from credentials import *

# Authentications
bot = praw.Reddit(user_agent='testBot v0.1',
client_id = CLIENT_ID,
client_secret = CLIENT_SECRET,
username = USERNAME,
password = PASSWORD)

# Pointing testBot to r/clevelandcavs
subreddit = bot.subreddit('clevelandcavs')

# Monitor r/clevelandcavs for new comments with generator
comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author
    if 'lebron' in text.lower():
        # Generate message
        message = "BelieveLand, u/{0}".format(author)

        comment.reply(message) # Send message
