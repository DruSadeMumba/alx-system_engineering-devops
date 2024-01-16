#!/usr/bin/python3
"""Recursive function to query Reddit API and get titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Queries the Reddit API"""
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'com.drusade/2.0 (rrr47)'
    }
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    if 'error' in data:
        return None
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        title = post.get('data', {}).get('title', '')
        hot_list.append(title)
    after = data.get('data', {}).get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
