"""
Danbooru site surfer
"""
import json

import requests

from src.locations._booru import _booru

DAN_URL = "https://danbooru.donmai.us/posts.json?limit=1&page=1"

class danbooru():
    name = "Danbooru"
    _order_param = "order:random"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from danbooru

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        imaged = _booru.search(DAN_URL, danbooru._order_param, tags, rating)
        return imaged.get("file_url") if imaged else None
