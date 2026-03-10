import snscrape.modules.twitter as sntwitter
import feedparser
import json

data=[]

# TWITTER / X
for tweet in sntwitter.TwitterSearchScraper("Belitung UMKM digital").get_items():

    data.append({
        "source":"X",
        "text":tweet.content,
        "url":tweet.url
    })

    if len(data)>15:
        break


# GOOGLE NEWS
news = feedparser.parse(
"https://news.google.com/rss/search?q=UMKM+Belitung"
)

for entry in news.entries[:10]:

    data.append({
        "source":"Google News",
        "text":entry.title,
        "url":entry.link
    })


# YOUTUBE
yt = feedparser.parse(
"https://www.youtube.com/feeds/videos.xml?search_query=UMKM+Belitung"
)

for entry in yt.entries[:10]:

    data.append({
        "source":"YouTube",
        "text":entry.title,
        "url":entry.link
    })


with open("data.json","w",encoding="utf8") as f:
    json.dump(data,f,indent=2,ensure_ascii=False)