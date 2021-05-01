"""
Gelbooru site surfer
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
GEL_URL = "https://gelbooru.com//index.php?page=dapi&s=post&q=index&json=1&pid=1&limit=1&tags={rating_param}sort:random+{tags}"

class gelbooru():
    name = "Gelbooru"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from gelbooru

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        url = GEL_URL.format(tags=tags, rating_param=(RATING_PARAM.format(rating=_RATING_MAP[rating]) if rating else ""))
        gel_res = requests.get(url)

        if not gel_res.ok:
            gel_res.raise_for_status()
        # Gelbooru returns an empty, but 200 status response if there are no matches sometimes...
        if not gel_res.text:  # No results
            return None
        gel_json = gel_res.json()
        if not gel_json:  # No results
            return None
        gel_json = gel_res.json()[0]
        return gel_json.get("file_url")
