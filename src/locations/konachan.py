"""
Konachan site surfer
"""
import json

import requests

KONA_URL = "https://konachan.com/post.json?page=1&limit=1&tags={tags}"



def konachan(tags):
    """
    Fetch image from konachan

    :param str tags: tags to search for

    :returns: image URL
    :rtype: str
    """
    kona_chan = requests.get(KONA_URL.format(tags=tags)).json()
    if kona_chan:
        return kona_chan[0]['file_url']
    return None