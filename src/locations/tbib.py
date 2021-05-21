"""
The Big Image Board site surfer
"""
import json

import requests

from src.locations._booru import _booru

TBIB_URL = "https://tbib.org/index.php?page=dapi&s=post&json=1&q=index&pid=1&limit=1"

class tbib():
    name = "The Big Image Board"
    # There's no random sort here, use "pseudo-random" latest updated.
    _order_param = "sort:updated:desc"
    _image_base_url = "https://tbib.org/images/{directory}/{file}"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from TBIB

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        imaged = _booru.search(TBIB_URL, tbib._order_param, tags, rating)
        # TBIB normally returns XML. The JSON return doesn't include the full filepath directly for whatever reason.
        # We can reconstruct it though.
        if imaged:
            try:
                return tbib._image_base_url.format(directory=imaged["directory"], file=imaged["image"])
            except KeyError:
                return None
        return None
