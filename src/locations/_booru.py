"""
Abstract booring class, as most boorus share some similarity in the way they are structured.
"""
import json

import requests

_RATING_MAP = {
    "safe": "safe",
    "questionable": "questionable",
    "explicit": "explicit"
}

RATING_PARAM = "rating:{rating}+"
SORT_PARAM = "{sort_order}+"
GENERIC_URL = "{url}&tags={rating_param}{sort_param}{tags}"

class _booru():
    @staticmethod
    def search(url, sort, tags, rating, **request_params):
        """
        Fetch image from a booru

        :param str url: Base URL to the booru in question
        :param str sort: Whichever sort the booru takes
        :param str tags: The formatted tag string to search for
        :param str rating: the requested rating
        :param **request_params: any additional parameters to be used in the requests.get call. Useful for headers/auth

        :returns: image URL
        :rtype: str
        """
        url = GENERIC_URL.format(
            url=url,
            rating_param=(RATING_PARAM.format(rating=_RATING_MAP[rating]) if rating else ""),
            sort_param=(SORT_PARAM.format(sort_order=sort) if sort else ""),
            tags=tags,
            
        )
        res = requests.get(url, **request_params)

        if res.status_code == 422:
            # Danbooru doesn't allow searches on more than two tags unless you're premium.
            # For whatever reason, rating: and order: together count as one tag.
            # Probably a bug on their end, but we need to catch mega-queries anyway.
            # Put in the abtract class as it doesn't affect other sites, and could be applicable
            # for future additions.
            return None
        if not res.ok:
            res.raise_for_status()
        if not res.text:
            # Gelbooru returns an empty, but 200 status response if there are no matches sometimes...
            # Seems to only apply to Gelbooru, but the failsafe logic is valid everywhere, so it's put here.
            return None
        res_json = res.json()
        if not res_json:  # No results
            return None
        return res_json[0]
