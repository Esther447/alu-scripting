#!/usr/bin/python3
"""
Reddit API Module - Debugging Version
"""
import requests


def top_ten(subreddit):
    """
    Fetch and print the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None: Prints the top 10 post titles or 'None' if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    # Debug: Print API URL
    print(f"Debug: Requesting {url}")

    # Make request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Debug: Print response status and content
    print(f"Debug: Status Code = {response.status_code}")
    print(f"Debug: Response JSON = {response.json()}")

    # Check for errors
    if response.status_code != 200:
        print("None")  # Match expected behavior
        return

    # Extract post data
    data = response.json().get('data', {})
    posts = data.get('children', [])

    if not posts:
        print("None")
        return

    # Print the top 10 post titles
    for post in posts:
        print(post['data'].get('title', 'No Title'))
#!/usr/bin/python3
"""
Reddit API Module - Debugging Version
"""
import requests


def top_ten(subreddit):
    """
    Fetch and print the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None: Prints the top 10 post titles or 'None' if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    # Debug: Print API URL
    print(f"Debug: Requesting {url}")

    # Make request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Debug: Print response status and content
    print(f"Debug: Status Code = {response.status_code}")
    print(f"Debug: Response JSON = {response.json()}")

    # Check for errors
    if response.status_code != 200:
        print("None")  # Match expected behavior
        return

    # Extract post data
    data = response.json().get('data', {})
    posts = data.get('children', [])

    if not posts:
        print("None")
        return

    # Print the top 10 post titles
    for post in posts:
        print(post['data'].get('title', 'No Title'))
