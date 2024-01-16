#!/usr/bin/python3
"""Recursive function to count occurrences of keywords in hot articles"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Queries the Reddit API"""
    if word_count is None:
        word_count = {}
    if not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'com.drusade/2.0 (rrr47)'
    }
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return

    data = response.json()
    if 'error' in data:
        return

    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            if f" {word} " in f" {title} ":
                word_count[word] = word_count.get(word, 0) + 1
    after = data.get('data', {}).get('after')
    if after is not None:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word}: {count}")
