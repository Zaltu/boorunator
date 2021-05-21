"""
Sankaku site surfer
"""
import json

import requests

from src.locations._booru import _booru

# Sankaku API expects a header, to help prevent bot spam
_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

SANKAKU_URL = "https://capi-v2.sankakucomplex.com/posts?lang=en&page=1&limit=1"

class sankaku():
    name = "Sankaku Complex"
    _order_param = "order:random"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from konachan

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        imaged = _booru.search(SANKAKU_URL, sankaku._order_param, tags, rating, headers=_HEADERS)
        return imaged.get("file_url") if imaged else None
