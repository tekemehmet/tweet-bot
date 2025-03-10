import feedparser

def fetch_mtb_news():
    url = "https://news.google.com/rss/search?q=mountain+biking"
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries[:5]:  # Limit to 5 articles
        articles.append({"title": entry.title, "link": entry.link})
    
    return articles
