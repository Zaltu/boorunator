"""
Search image hosting servers for images matching certain tags.
"""
import re
import requests
from src.consts import sites, ratings, TAG_REGEX, _DEFAULT_ORDER, NoResult, BadTag
# Sties, ratings used to simplify imports

def _findfrom(tagstr, rating, fromsite):
    """
    Try and find an image matching the tags from a specific site.

    :param str tagstr: param-formatted tagstring, see `boorunator.sanitize`
    :param ratings rating: rating constant enum
    :param sites fromsite: site (class) to search in

    :raises NoResult: if the search returns no images for that site, or an HTTP error was raised

    :return: image url
    :rtype: str
    """
    try:
        image_url = fromsite.search(tagstr, rating)
    except requests.HTTPError as e:
        raise NoResult("An unexpected HTTP error occured:\n%s" % str(e))
    if not image_url:
        raise NoResult(f"No result found for tags {tagstr} and rating {rating} at {fromsite.name}")
    return image_url


def _findonethrougout(tagstr, rating):
    """
    Try each site in predetermined order to find an image.

    :param str tagstr: param-formatted tagstring, see `boorunator.sanitize`
    :param ratings rating: rating constant enum

    :raises NoResult: if the search returns no images for any site

    :return: image url
    :rtype: str
    """
    for source in _DEFAULT_ORDER:
        try:
            return _findfrom(tagstr, rating, source)
        except NoResult:
            pass
    # If we get to this point, nothing has returned a result...
    raise NoResult(f"No result found for tags {tagstr} and rating {rating}")


def sanitize(tags):
    """
    Convert a tag list into booru-style URL parameters.

    :param list[str] tags: tags to use

    :raises BadTag: if an invalid tag is detected

    :return: URL-ready parameters for boorus
    :rtype: str
    """
    if not tags:
        raise BadTag(f"No tags submitted: {tags}")
    temp = []
    for tag in tags:
        # Strip trailing and starting whitespaces
        tag = tag.strip()
        # Check for string format/unacceptable special characters
        if not re.fullmatch(TAG_REGEX, tag):
            raise BadTag(f"ERROR: invalid tag detected. Tags should be in {TAG_REGEX}, but found {tag}")
        # Check if tag is empty. Should be handled by regex above, but hey
        if not tag or tag.isspace():
            raise BadTag(f"ERROR: No tags found in \"{tag}\"")

        if " " in tag:
            temp.append(tag.lower().replace(" ", "_"))
        else:
            temp.append(tag.lower())
    return "+".join(temp)


def boor(tags, rating=None, fromsite=None):
    """
    Search the web for weeb pictures matching requested tags and rating, optionally from a specific known site.

    :param list[str] tags: list of tags. See ReadMe for formatting information
    :param ratings rating: the rating of the image, default all
    :param sites fromsite: the known site to search, defaults src.consts._DEFAULT_ORDER

    :raises BadTag: if one or more of the provided tags are not useable
    :raises NoResult: if no images could be found matching the requested parameters

    :return: image url
    :rtype: str
    """
    tagstr = sanitize(tags)
    if not fromsite:
        return _findonethrougout(tagstr, rating)
    else:
        return _findfrom(tagstr, rating, fromsite)
