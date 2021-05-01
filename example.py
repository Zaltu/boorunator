from src import boorunator

rating = boorunator.ratings.SAFE
fromsite = boorunator.sites.SANKAKU
tags = ["elf", "white hair"]

image_url = boorunator.boor(tags, rating=rating)
print(image_url)
