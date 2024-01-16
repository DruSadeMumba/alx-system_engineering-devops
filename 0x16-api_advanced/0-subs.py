#!/usr/bin/python3
"""A func that queries the Reddit API and returns the num of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, allow_redirects=False)
        data = response.json()
        if 'error' in data or response.status_code != 200:
            return 0
        return data['data']['subscribers']
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
