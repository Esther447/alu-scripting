#!/usr/bin/python3
"""Module to recursively retrieve hot post titles from a subreddit."""

import requests  # E402 - Ensure import is at the top

def recurse(subreddit, hot_list=None, after=None):
    """Recursively retrieves hot post titles from a subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    json_res = response.json()
    after = json_res.get('data', {}).get('after')  # Gets next page token
    hot_articles = json_res.get('data', {}).get('children', [])

    for article in hot_articles:
        hot_list.append(article.get('data', {}).get('title'))  # Append post title

    return recurse(subreddit, hot_list, after=after) if after else hot_list
