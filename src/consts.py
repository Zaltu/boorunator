from src.locations.konachan import konachan
from src.locations.danbooru import danbooru
from src.locations.gelbooru import gelbooru
from src.locations.sankaku import sankaku
from src.locations.tbib import tbib


class sites():
    """
    Namespace for booru options
    """
    KONACHAN = konachan
    GELBOORU = gelbooru
    DANBOORU = danbooru
    SANKAKU = sankaku
    BIGIMAGEBOARD = tbib
class ratings():
    """
    Namespace for ratings
    TODO
    """
    SAFE = "safe"
    QUESTIONABLE = "questionable"
    EXPLICIT = "explicit"


TAG_REGEX = "[0-9a-zA-Z_() ]+"


_DEFAULT_ORDER = [sites.KONACHAN, sites.SANKAKU, sites.GELBOORU, sites.DANBOORU, sites.BIGIMAGEBOARD]


class NoResult(Exception):
    """
    No image matching the requested tags could be found across all sites.
    """
class BadTag(Exception):
    """
    A tag is not valid/has special characters...
    """
