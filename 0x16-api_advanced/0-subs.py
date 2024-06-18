#!/usr/bin/python3


import requests


def number_of_subscribrs(subredit):
    """function to get number of subs in a subreddit"""

    url = f"https://www.reddit.com/r/{subredit}/about.json"
    resp = requests.get(url=url).json()

    try:
        subs = resp.get("data").get("subscribers")
        return subs
    except Exception:
        return 0


if __name__ == "__main__":
    res = number_of_subscribrs("programming")
    print(res)
