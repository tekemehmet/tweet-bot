import os
import tweepy
import openai
from dotenv import load_dotenv

class Authentication:
    """
    Handles authentication for Twitter and OpenAI APIs.
    """
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Check if all required Twitter credentials exist
        self.twitter_consumer_key = os.getenv("TWITTER_CONSUMER_API_KEY")
        self.twitter_consumer_secret = os.getenv("TWITTER_CONSUMER_API_SECRET")
        self.twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.twitter_access_secret = os.getenv("TWITTER_ACCESS_SECRET")
        
        if not all([
            self.twitter_consumer_key,
            self.twitter_consumer_secret,
            self.twitter_access_token,
            self.twitter_access_secret
        ]):
            raise ValueError("Missing Twitter API credentials in .env file")
        
        # OpenAI credentials
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        
        # Initialize clients as None
        self.twitter_client = None
        self.openai_client = None

    def authenticate_twitter(self):
        """
        Authenticates with Twitter API and verifies credentials.
        """
        try:
            self.twitter_client = tweepy.Client(
                consumer_key=self.twitter_consumer_key,
                consumer_secret=self.twitter_consumer_secret,
                access_token=self.twitter_access_token,
                access_token_secret=self.twitter_access_secret
            )
            
            # Verify credentials by making a test API call
            try:
                self.twitter_client.get_me()
                print("Twitter authentication successful")
                return self.twitter_client
            except tweepy.TweepyException as e:
                if "403" in str(e):
                    print("Authentication failed: Your Twitter API credentials don't have the required permissions")
                    print("Please check your Twitter Developer Portal and ensure you have Write permissions")
                else:
                    print(f"Twitter API error: {e}")
                return None
                
        except Exception as e:
            print(f"Twitter authentication failed: {e}")
            return None

    def authenticate_openai(self):
        """
        Authenticates with OpenAI API and returns client.
        """
        try:
            openai.api_key = self.openai_api_key
            self.openai_client = openai
            print("OpenAI authentication successful")
            return self.openai_client
        except Exception as e:
            print(f"OpenAI authentication failed: {e}")
            return None

    def get_twitter_client(self):
        """
        Returns authenticated Twitter client or creates new one if none exists.
        """
        if not self.twitter_client:
            return self.authenticate_twitter()
        return self.twitter_client

    def get_openai_client(self):
        """
        Returns authenticated OpenAI client or creates new one if none exists.
        """
        if not self.openai_client:
            return self.authenticate_openai()
        return self.openai_client 