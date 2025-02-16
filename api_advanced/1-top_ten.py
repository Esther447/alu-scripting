#!/usr/bin/python3
"""
Module 1-top_ten
Contains a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
"""
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    if not isinstance(subreddit, str) or not subreddit:  # Handle invalid input
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} # Add a User-Agent

    try:
        response = requests.get(url, headers=headers, allow_redirects=False) # Prevent redirects
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        data = response.json()

        if 'data' in data and 'children' in data['data']:
          posts = data['data']['children']
          if not posts: # Handle empty subreddits
              print(None)
              return

          for post in posts:
              title = post['data']['title']
              print(title)
        else:
          print(None) # Handle unexpected JSON structure
          
    except requests.exceptions.RequestException as e:
        print(None)  # Print None for any request errors
    except (KeyError, TypeError): # Handle potential JSON parsing errors
        print(None)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
