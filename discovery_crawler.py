import instaloader
import pandas as pd

from ai_engine.business_detector import detect_business
from processing.location_detector import is_belitung

L = instaloader.Instaloader()

hashtags = [

"belitung",
"kulinerbelitung",
"oleholehbelitung",
"belitungfood",
"umkmbelitung",
"belitungolshop"

]

data = []

for tag in hashtags:

    print("Scanning hashtag:", tag)

    posts = instaloader.Hashtag.from_name(
        L.context,
        tag
    ).get_posts()

    for i, post in enumerate(posts):

        caption = post.caption

        if caption:

            if detect_business(caption) and is_belitung(caption):

                data.append({

                    "platform":"instagram",
                    "username":post.owner_username,
                    "caption":caption

                })

        if i > 100:
            break

df = pd.DataFrame(data)

df.drop_duplicates(
    subset="username",
    inplace=True
)

df.to_csv(
    "data/discovered_accounts.csv",
    index=False
)

print("Total akun ditemukan:", len(df))