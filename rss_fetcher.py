import feedparser
import requests


def shorten_url(url):
    api_url = "https://tinyurl.com/api-create.php"
    response = requests.get(api_url, params={"url": url})
    return response.text if response.status_code == 200 else url  # Fallback to original if API fails



def fetch_mtb_news():
    url = "https://news.google.com/rss/search?q=mountain+biking"
    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries[:2]:  # Limit to 2 articles
        short_link = shorten_url(entry.link)  # Convert to TinyURL
        articles.append({"title": entry.title, "link": short_link})
    
    return articles