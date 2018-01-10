#!/usr/bin/python3
"""recursive function that returns all hot articles of subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    reddit_hot = requests.get("https://www.reddit.com/r/{}/hot.json"
                              .format(subreddit),
                              headers={'user-agent': 'jvpupcat'},
                              allow_redirects=False,
                              params={'after': after})

    GetDataChildren = reddit_hot.json().get('data').get('children')
    for key in GetDataChildren:
        title = key.get('data').get('title')
        hot_list.append(title)
    after = reddit_hot.json().get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
