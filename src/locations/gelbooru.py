"""
Gelbooru site surfer
"""
import json

import requests

from src.locations._booru import _booru

GEL_URL = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&pid=1&limit=1"

class gelbooru():
    name = "Gelbooru"
    _order_param  = "sort:random"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from gelbooru

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        imaged = _booru.search(GEL_URL, gelbooru._order_param, tags, rating)
        return imaged.get("file_url") if imaged else None
