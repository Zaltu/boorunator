"""
Konachan site surfer
"""
import json

import requests

from src.locations._booru import _booru

KONA_URL = "https://konachan.com/post.json?page=1&limit=1"

class konachan():
    name = "Konachan"
    _order_param = "order:random"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from konachan

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        imaged = _booru.search(KONA_URL, konachan._order_param, tags, rating)
        return imaged.get("file_url") if imaged else None
