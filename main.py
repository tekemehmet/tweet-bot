from twitter_auth import authenticate_twitter
from rss_fetcher import fetch_mtb_news
from summarizer import summarize_and_translate

def main():
    api = authenticate_twitter()
    news_list = fetch_mtb_news()

    for news in news_list:
        summary = summarize_and_translate(news)
        tweet = f"{summary}\n\nKaynak: {news['link']}"
        api.update_status(tweet)
        print(f"Tweeted: {tweet}")

if __name__ == "__main__":
    main()
