#!/usr/bin/python3
"""func that prints top hot posts from Reddit"""

import requests


def top_ten(subreddit):
    reddit_url = requests.get("https://www.reddit.com/r/{}/hot.json".format(subreddit), params={'limit': 10}, headers={'user-agent': 'jvpupcat'}, allow_redirects=False)
    TopTen = reddit_url.json().get('data').get('children')
    if len(TopTen) == 0:
        print('None')
    for child in TopTen:
        title = child.get('data').get('title')
        print(title)
