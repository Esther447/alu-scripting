#!/usr/bin/python3
"""
Reddit API Query Module

This module contains a function to query the Reddit API and print the tittles of the first
"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json().get("data", {}).get("children", [])
    
    if not data:
        print(None)
        return
    
    for post in data:
        print(post["data"].get("title"))
