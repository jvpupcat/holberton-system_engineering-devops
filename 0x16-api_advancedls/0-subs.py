#!/usr/bin/python3
"""function that returns # of subscribers from Reddit API"""

import requests
import json

def number_of_subscribers(subreddit):
    """Queries number of subscribers for subreddit"""
    if type(subreddit) is not str:
        return 0
    reddit_url = ("https://www.reddit.com/r/{}/about.json".format(subreddit), {'user-agent': 'someone153'})
    NumOfSubcribers = requests.reddit_url.get('data').get('subscribers')
    if NumOfSubscribers is None:
        return 0
    return NumOfSubscribers.json().get('data').get('subscribers')
