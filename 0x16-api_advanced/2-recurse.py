#!/usr/bin/python3
"""recursive function that returns all hot articles of subreddit"""

import requests


def recurse(subreddit, hot_list[], after)
    reddit_hot = requests.get("https://www.reddit.com/r/{}/hot.json"
                              .format(subreddit),
                              headers={'user-agent': 'jvpupcat'},
                              allow_redirects=False,
                              params=)

    GetDataChildren = reddit_hot.json().get('data').get('children')
    title = key.get('data').get('title')
    hot_list = hot_list.append(title)
    if after is None:
        return hot_list
    recurse(subreddit, hot_list, after)
