#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API
to return a list of titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches all hot post titles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list storing the titles of hot posts.
        after (str): The pagination parameter to get the next page.

    Returns:
        list: A list of hot post titles, or None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditBot/1.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None  # Invalid subreddit

    try:
        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            return hot_list if hot_list else None

        hot_list.extend(post["data"]["title"] for post in posts)

        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)

        return hot_list
    except Exception:
        return None
