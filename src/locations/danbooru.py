"""
Danbooru site surfer
"""
import json

import requests

DAN_URL = "https://danbooru.donmai.us/posts.json?limit=1&page=1&tags={tags}"

def danbooru(tags):
    """
    Fetch image from danbooru

    :param str tags: tags to search for

    :returns: image URL
    :rtype: str
    """
    booru_chan = requests.get(DAN_URL.format(tags=tags)).json()
    if booru_chan:
        return booru_chan[0]['file_url']
    return None