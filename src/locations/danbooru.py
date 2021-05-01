"""
Danbooru site surfer
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
DAN_URL = "https://danbooru.donmai.us/posts.json?limit=1&page=1&tags={rating_param}{tags}"


class danbooru():
    name = "Danbooru"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from danbooru

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        url = DAN_URL.format(tags=tags, rating_param=(RATING_PARAM.format(rating=_RATING_MAP[rating]) if rating else ""))
        dan_res = requests.get(url)

        if not dan_res.ok:
            dan_res.raise_for_status()
        dan_json = dan_res.json()
        if not dan_json:  # No results
            return None
        dan_json = dan_json[0]
        return dan_json.get("file_url")
