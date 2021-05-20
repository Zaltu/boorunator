"""
The Big Image Board site surfer
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
# There's no random sort here, use pseudo-random latest updated.
TBIB_URL = "https://tbib.org/index.php?page=dapi&s=post&json=1&q=index&pid=1&limit=1&tags={rating_param}+sort:updated:desc+{tags}"

class tbib():
    name = "The Big Image Board"
    _image_base_url = "https://tbib.org/images/{directory}/{file}"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from TBIB

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        url = TBIB_URL.format(tags=tags, rating_param=(RATING_PARAM.format(rating=_RATING_MAP[rating]) if rating else ""))
        tbib_res = requests.get(url)

        if not tbib_res.ok:
            tbib_res.raise_for_status()

        tbib_json = tbib_res.json()
        if not tbib_json:  # No results
            return None
        tbib_json = tbib_json[0]
        # TBIB normally returns XML. The JSON return doesn't include the full filepath directly for whatever reason.
        # We can reconstruct it though.
        try:
            return tbib._image_base_url.format(directory=tbib_json["directory"], file=tbib_json["image"])
        except KeyError:
            return None
