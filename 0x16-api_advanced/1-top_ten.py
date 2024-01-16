#!/usr/bin/python3
"""Queries the Reddit API and prints titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'com.drusade/2.0 (rrr47)'
    }
    params = {'limit': 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    if 'error' in data:
        print(None)
        return
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        title = post.get('data', {}).get('title', '')
        print(title)
