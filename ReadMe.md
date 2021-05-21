# Boorunator
Easily fetch a single image from one or more of various image hosting services. AIGIS plugin.

This could pretty easily be converted into a scraper, but that's not really the goal of this repo. We just want to get one pseudo-random image based on search preferences.

# Use
```python
import boorunator
tags = ["elf", "white hair"]
rating = boorunator.ratings.SAFE
fromsite = boorunator.sites.KONACHAN
image_url = boorunator.boor(tags, rating=rating, fromsite=fromsite)
```

`fromsite` is not required. By default, boorunator will search the following, in order:
1. Sankaku Complex
2. Konachan
3. Gelbooru
4. Danbooru
5. The Big Image Board

`rating` is not required. By default, all images are accepted.  
__This means the search result should be considered NSFW if no rating is specified__.