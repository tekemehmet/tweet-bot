import os
import tweepy
from dotenv import load_dotenv
from summarizer import summarize_and_translate
from rss_fetcher import fetch_mtb_news
from utils import load_posted_news, save_posted_news

load_dotenv()

# Twitter API kimlik bilgileri
CONSUMER_API_KEY = os.getenv("TWITTER_CONSUMER_API_KEY")
CONSUMER_API_SECRET = os.getenv("TWITTER_CONSUMER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Twitter API'ye bağlan
client = tweepy.Client(
    consumer_key=CONSUMER_API_KEY,
    consumer_secret=CONSUMER_API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Daha önce paylaşılan haberleri yükle
posted_news = load_posted_news()

# Haberleri çek
news_list = fetch_mtb_news()

# İlk paylaşılmamış haberi bul
news_to_post = None
for news in news_list:
    if news["title"] not in posted_news:
        news_to_post = news
        break  # İlk uygun haberi bulduk, döngüden çık

if news_to_post:
    summary = summarize_and_translate(news_to_post)
    tweet_text = f"{summary}\n\n#MTB #MountainBiking"

    # Tweet paylaş
    try:
        response = client.create_tweet(text=tweet_text)
        tweet_id = response.data["id"]
        print(f"Tweet paylaşıldı: {tweet_text}")

        # Kaynağı yanıt olarak ekleyelim
        client.create_tweet(text=f"Kaynak: {news_to_post['link']}", in_reply_to_tweet_id=tweet_id)

        # Paylaşılan haberi kaydet
        save_posted_news(news_to_post["title"])
    except tweepy.TweepyException as e:
        print(f"Tweet paylaşılırken hata oluştu: {e}")
else:
    print("Yeni haber bulunamadı, daha sonra tekrar dene.")

