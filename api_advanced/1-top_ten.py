#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None: Prints the top 10 post titles or 'None' if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        print("None")
        return

    for post in posts[:10]:
        print(post["data"].get("title", "No Title"))
