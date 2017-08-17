import praw
from credentials import *

bot = praw.Reddit(user_agent='testBot v0.1',
client_id=CLIENT_ID
client_secret=CLIENT_SECRET
username=USERNAME
password=PASSWORD
)
