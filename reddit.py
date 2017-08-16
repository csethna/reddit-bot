# 1. Fetch comments
# 2. Process those comments
# 3. Sleep for some time
# 4. Go to 1

import praw
import time

# Initialize PRAW with a custom User-Agent

r = praw.Reddit('Simple comment parser from WhyCouch')

polite_users = set() # avoids duplicates

for i in xrange(0, 10): # runs loop 10 times
    comments = r.get_comments('askreddit')
    for comment in comments:
        body = comment.body.lower()
        if body.find("thank") != -1 or body.find("please") != -1:
            polite_users.add(comment.author)
    time.sleep(120) # sleep for 2 minutes

    print("The polite users were :")
    for user in polite_users:
        print(user)
