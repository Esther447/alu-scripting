#!/usr/bin/python3
"""Module to print the titles of the top 10 hot posts from a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}  # Fetch only 10 posts

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    if not children:
        print(None)
        return

    for post in children:
        print(post.get('data', {}).get('title', 'No Title'))
