import feedparser
import requests

# RSS kaynak listesi
RSS_FEEDS = [
    "https://news.google.com/rss/search?q=mountain+biking",
    "https://www.pinkbike.com/news/rss/",
    "https://www.mtb-news.de/news/feed/",
    "https://www.bikeradar.com/feed/",
    "https://www.singletracks.com/feed/"
]

def shorten_url(url):
    """TinyURL API kullanarak linki kısaltır."""
    api_url = "https://tinyurl.com/api-create.php"
    response = requests.get(api_url, params={"url": url})
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"⚠️ TinyURL başarısız oldu, orijinal link kullanılıyor: {url}")
        return url  # API başarısız olursa orijinal linki kullan

def fetch_mtb_news():
    """Belirtilen RSS kaynaklarından haberleri çeker ve döndürür."""
    articles = []

    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        
        for entry in feed.entries[:3]:  # Her kaynaktan en fazla 3 haber al
            short_link = shorten_url(entry.link)  # TinyURL ile linki kısalt
            articles.append({"title": entry.title, "link": short_link})

    return articles
