import os
import tweepy
from dotenv import load_dotenv
from summarizer import summarize_and_translate
from rss_fetcher import fetch_mtb_news
from utils import load_posted_news, save_posted_news
from auth import Authentication

def post_mtb_news():
    """
    Fetches mountain biking news, translates, and posts to Twitter.
    Handles previously posted news tracking and error handling.
    """
    # Initialize authentication
    auth = Authentication()
    
    # Get authenticated clients
    client = auth.get_twitter_client()
    openai_client = auth.get_openai_client()
    
    if not client or not openai_client:
        print("Authentication failed")
        return False

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
        tweet_text = f"{summary}\n#MountainBiking\nHaberin linki altta "
        print(tweet_text)

        # Tweet paylaş
        try:
            response = client.create_tweet(text=tweet_text)
            tweet_id = response.data["id"]
            print(f"Tweet paylaşıldı: {tweet_text}")

            # Kaynağı yanıt olarak ekleyelim
            client.create_tweet(text=f"Kaynak: {news_to_post['link']}", in_reply_to_tweet_id=tweet_id)

            # Paylaşılan haberi kaydet
            save_posted_news(news_to_post["title"])
            return True
        except tweepy.TweepyException as e:
            print(f"Tweet paylaşılırken hata oluştu: {e}")
            return False
    else:
        print("Yeni haber bulunamadı, daha sonra tekrar dene.")
        return False

if __name__ == "__main__":
    post_mtb_news()
