#!/usr/bin/python3
"""A func that queries the Reddit API and returns the num of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'com.drusade/2.0 (rrr47)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    data = response.json()
    if 'error' in data:
        return 0
    return data['data']['subscribers']
