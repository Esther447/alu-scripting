#!/usr/bin/python3
"""
Queries the Reddit API to print the top 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: Prints top 10 post titles or "None" if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditBot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post["data"]["title"])
    except Exception:
        print("None")
