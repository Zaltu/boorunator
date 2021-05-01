"""
Sankaku site surfer
"""
import json
import requests

# Sankaku API expects a header, to help prevent bot spam
_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
# Hee hee
_RATING_MAP = {
    "safe": "safe",
    "questionable": "questionable",
    "explicit": "explicit"
}

RATING_PARAM = "rating:{rating}+"
SANKAKU_URL = "https://capi-v2.sankakucomplex.com/posts?lang=en&page=1&limit=1&tags={rating_param}order:random+{tags}"

class sankaku():
    name = "Sankaku Complex"
    @staticmethod
    def search(tags, rating):
        """
        Fetch image from konachan

        :param str tags: tags to search for

        :returns: image URL
        :rtype: str
        """
        url = SANKAKU_URL.format(tags=tags, rating_param=(RATING_PARAM.format(rating=_RATING_MAP[rating]) if rating else ""))
        sankaku_res = requests.get(url, headers=_HEADERS)

        if not sankaku_res.ok:
            sankaku_res.raise_for_status()
        sankaku_json = sankaku_res.json()
        if not sankaku_json:  # No results
            return None
        sankaku_json = sankaku_json[0]
        #print(sankaku_json.get("rating"))
        #print(str(sankaku_json.get("width")) + "x" + str(sankaku_json.get("height")))
        return sankaku_json.get("file_url")
