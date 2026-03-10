import requests
import feedparser
from bs4 import BeautifulSoup
import json

data=[]

headers={
"User-Agent":"Mozilla/5.0"
}

# =========================
# GOOGLE NEWS
# =========================

def google_news():

    url="https://news.google.com/rss/search?q=Belitung+UMKM+digital"

    feed=feedparser.parse(url)

    for item in feed.entries[:20]:

        data.append({
            "source":"Google News",
            "title":item.title,
            "link":item.link
        })


# =========================
# YOUTUBE
# =========================

def youtube():

    url="https://www.youtube.com/feeds/videos.xml?search_query=Belitung+UMKM+digital"

    feed=feedparser.parse(url)

    for item in feed.entries[:10]:

        data.append({
            "source":"YouTube",
            "title":item.title,
            "link":item.link
        })


# =========================
# X / TWITTER
# =========================

def twitter():

    url="https://nitter.net/search/rss?f=tweets&q=Belitung+UMKM+digital"

    feed=feedparser.parse(url)

    for item in feed.entries[:20]:

        data.append({
            "source":"X",
            "title":item.title,
            "link":item.link
        })


# =========================
# REDDIT
# =========================

def reddit():

    url="https://www.reddit.com/search.rss?q=Belitung+UMKM"

    feed=feedparser.parse(url)

    for item in feed.entries[:20]:

        data.append({
            "source":"Reddit",
            "title":item.title,
            "link":item.link
        })


# =========================
# TIKTOK SCRAPER
# =========================

def tiktok():

    url="https://www.tiktok.com/search?q=belitung%20umkm"

    r=requests.get(url,headers=headers)

    soup=BeautifulSoup(r.text,"html.parser")

    links=soup.find_all("a")

    for l in links[:20]:

        href=l.get("href")

        if href and "/video/" in href:

            data.append({
                "source":"TikTok",
                "title":"TikTok Video",
                "link":"https://www.tiktok.com"+href
            })


# =========================
# INSTAGRAM HASHTAG
# =========================

def instagram():

    url="https://www.instagram.com/explore/tags/belitung/"

    r=requests.get(url,headers=headers)

    soup=BeautifulSoup(r.text,"html.parser")

    links=soup.find_all("a")

    for l in links[:20]:

        href=l.get("href")

        if href and "/p/" in href:

            data.append({
                "source":"Instagram",
                "title":"Instagram Post",
                "link":"https://www.instagram.com"+href
            })


# =========================
# PORTAL BERITA BABEL
# =========================

def berita_babel():

    sites=[
        "https://babelpos.disway.id",
        "https://bangkapos.com",
        "https://wowbabel.com"
    ]

    for site in sites:

        try:

            r=requests.get(site,headers=headers,timeout=10)

            soup=BeautifulSoup(r.text,"html.parser")

            links=soup.find_all("a")

            for l in links[:30]:

                text=l.get_text().lower()

                if "belitung" in text or "umkm" in text or "digital" in text:

                    data.append({
                        "source":site,
                        "title":l.get_text().strip(),
                        "link":l.get("href")
                    })

        except:
            pass


# =========================
# RUN ALL CRAWLER
# =========================

google_news()
youtube()
twitter()
reddit()
tiktok()
instagram()
berita_babel()


# =========================
# SAVE
# =========================

with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=2,ensure_ascii=False)

print("Crawler selesai. Total data:",len(data))
