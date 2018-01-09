#!/usr/bin/python3
"""function that returns # of subscribers from Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """Queries number of subscribers for subreddit"""
    if type(subreddit) is not str:
        return 0
    try:
        reddit_url = requests.get("https://www.reddit.com/r/{}/about.json"
                                  .format(subreddit),
                                  headers={'user-agent': 'jvpupcat'},
                                  allow_redirects=False)
        NumOfSubscribers = reddit_url.json().get('data').get('subscribers')
    except AttributeError:
        return 0
    if NumOfSubscribers is None:
        return 0
    return NumOfSubscribers
