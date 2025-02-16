#!/usr/bin/python3
"""DOCS"""
import requests


def top_ten(subreddit):
    """Docs"""
    reddit_url = f"https://www.reddit.com/r/{}/hot.json" \
    headers = {'User-agent': 'Mozilla/5.0'}


    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get['data', {}]
        children = data.get('children', [])

        for post in children[:10]:
            print(post.get('data', {}).get('title', 'No Title'))
    else:
        print(None)
