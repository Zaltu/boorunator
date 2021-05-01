from src.locations.konachan import konachan
from src.locations.danbooru import danbooru
from src.locations.gelbooru import gelbooru
from src.locations.sankaku import sankaku


class sites():
    """
    Namespace for booru options
    """
    KONACHAN = konachan
    GELBOORU = gelbooru
    DANBOORU = danbooru
    SANKAKU = sankaku
class ratings():
    """
    Namespace for ratings
    TODO
    """
    SAFE = "safe"
    QUESTIONABLE = "questionable"
    EXPLICIT = "explicit"


TAG_REGEX = "[0-9a-zA-Z_() ]+"


_DEFAULT_ORDER = [sites.SANKAKU, sites.KONACHAN, sites.GELBOORU, sites.DANBOORU]


class NoResult(Exception):
    """
    No image matching the requested tags could be found across all sites.
    """
class BadTag(Exception):
    """
    A tag is not valid/has special characters...
    """
