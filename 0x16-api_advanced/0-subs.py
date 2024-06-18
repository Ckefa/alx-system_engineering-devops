#!/usr/bin/env python3


import requests


def number_of_subscribrs(subredit):
    url = f"https://www.reddit.com/r/{subredit}/about.json"
    resp = requests.get(url=url).json()

    if not resp:
        return 0

    subs = resp.get("data").get("subscribers")
    if subs:
        return subs

    return 0


if __name__ == "__main__":
    res = number_of_subscribrs("programming")
    print(res)
