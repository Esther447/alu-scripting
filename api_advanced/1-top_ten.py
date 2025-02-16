#!/usr/bin/python3
"""DOCS"""
import requests


def top_ten(subreddit):
    """DOCS"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print(None)
            return

        for post in posts[:10]:
            print(post["data"]["title"])
    else:
        print(None)
