"""
Gelbooru site surfer
"""
import json

import requests

GEL_URL = "https://gelbooru.com//index.php?page=dapi&s=post&q=index&json=1&pid=1&limit=1&tags={tags}"

def gelbooru(tags):
    """
    Fetch image from gelbooru

    :param str tags: tags to search for

    :returns: image URL
    :rtype: str
    """
    try:
        gel_chan = requests.get(GEL_URL.format(tags=tags)).json()
    except json.decoder.JSONDecodeError:
        gel_chan = None
    if gel_chan:
        return gel_chan[0]['file_url']
    return None
