"""
Konachan site surfer
"""
import json

import requests

# Hee hee
_RATING_MAP = {
    "safe": "safe",
    "questionable": "questionable",
    "explicit": "explicit"
}

RATING_PARAM = "rating:{rating}+"
KONA_URL = "https://konachan.com/post.json?page=1&limit=1&tags={rating_param}order:random+{tags}"


class konachan():
    name = "Konachan"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from konachan

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        url = KONA_URL.format(tags=tags, rating_param=(RATING_PARAM.format(rating=_RATING_MAP[rating]) if rating else ""))
        kona_res = requests.get(url)

        if not kona_res.ok:
            kona_res.raise_for_status()
        kona_json = kona_res.json()
        if not kona_json:  # No results
            return None
        kona_json = kona_json[0]
        return kona_json.get("file_url")
