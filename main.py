import os 
import tweepy
from dotenv import load_dotenv
from summarizer import summarize_and_translate
from rss_fetcher import fetch_mtb_news

load_dotenv()

# Your Twitter API credentials
CONSUMER_API_KEY = os.getenv("TWITTER_CONSUMER_API_KEY")
CONSUMER_API_SECRET = os.getenv("TWITTER_CONSUMER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate with Twitter API v2
client = tweepy.Client(
    consumer_key=CONSUMER_API_KEY,
    consumer_secret=CONSUMER_API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

news_list = fetch_mtb_news()

for news in news_list:
    summary = summarize_and_translate(news)
    tweet_text = f"{summary}\n\nKaynak: {news['link']}"
    print(tweet_text)
        

# Function to post a tweet
def post_tweet(tweet_text):
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Successfully posted: {tweet_text}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

# Example usage
if __name__ == "__main__":
    # Simple tweet
    
    post_tweet(tweet_text)