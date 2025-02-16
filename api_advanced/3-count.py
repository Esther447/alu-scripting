#!/usr/bin/python3
"""
Module 3-count
Contains a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive).
"""
import requests
import re

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API and counts word occurrences in hot article titles.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        after (str, optional): The 'after' parameter for pagination. Defaults to None.
        counts (dict, optional): A dictionary to store word counts. Defaults to None.

    Returns:
        None
    """

    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0  # Initialize counts for all keywords

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    if after:
        url += f"&after={after}"

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                if 'data' in post and 'title' in post['data']:
                    title = post['data']['title'].lower()
                    for word in word_list:
                        keyword = word.lower()
                        # Count whole word occurrences using word boundaries
                        count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', title))
                        counts[keyword] += count

            after = data['data'].get('after')
            if after:
                count_words(subreddit, word_list, after, counts)  # Recursive call for pagination
            else:
                # Sort and print the results
                sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")

        else:
            return  # No posts or invalid subreddit, print nothing

    except requests.exceptions.RequestException:
        return  # Handle request errors, print nothing
    except (KeyError, TypeError, ValueError):
        return  # Handle JSON parsing errors, print nothing

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
