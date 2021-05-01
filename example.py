from src import boorunator

rating = boorunator.ratings.SAFE
fromsite = boorunator.sites.SANKAKU
tags = ["elf", "white hair"]

try:
    image_url = boorunator.boor(tags, rating=rating)
    print(image_url)
except (boorunator.BadTag, boorunator.NoResult) as e:
    print(str(e) + "\n:(")
