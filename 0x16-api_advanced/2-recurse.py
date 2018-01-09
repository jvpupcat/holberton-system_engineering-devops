#!/usr/bin/python3
"""recursive function that returns all hot articles of subreddit"""

import requests


def recurse(subreddit, hot_list[])
    reddit_url = requests.get("https://www.reddit.com/r/{}/hot.json"
                              .format(subreddit),
                              headers={'user-agent': 'jvpupcat'},
                              allow_redirects=False)
    try:
        
