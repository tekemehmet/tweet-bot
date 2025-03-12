# MTB News Twitter Bot

This project is a Twitter bot that fetches the latest mountain biking news from various RSS feeds, summarizes and translates them into Turkish, and posts them on Twitter with relevant hashtags. The bot also ensures that the same news is not posted twice and replies to its own tweet with a shortened link to the news source.

## Features
- Fetches mountain biking news from multiple RSS feeds.
- Summarizes and translates the news into Turkish using OpenAI's GPT model.
- Posts tweets with relevant hashtags.
- Avoids posting the same news twice by maintaining a history of posted articles.
- Shortens news links using TinyURL and posts them as replies to the main tweet.

## Installation

### Prerequisites
- Python 3.x
- Twitter Developer Account (for API keys)
- OpenAI API Key

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/mtb-news-bot.git
   cd mtb-news-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add the following credentials:
   ```env
   TWITTER_CONSUMER_API_KEY=your_consumer_api_key
   TWITTER_CONSUMER_API_SECRET=your_consumer_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_SECRET=your_access_secret
   OPENAI_API_KEY=your_openai_api_key
   ```
4. Run the bot:
   ```sh
   python main.py
   ```

## File Structure
- `main.py` - The main script that orchestrates fetching, summarizing, and posting news on Twitter.
- `rss_fetcher.py` - Fetches mountain biking news from multiple RSS feeds and shortens the URLs.
- `summarizer.py` - Summarizes and translates news articles using OpenAI's GPT model.
- `utils.py` - Handles saving and loading previously posted news.
- `posted_news.txt` - Stores titles of previously posted news to prevent duplicate tweets.

## Future Improvements
- Deploy the bot to Google Cloud and use Firestore instead of a `.txt` file.
- Schedule automatic tweets using a cloud function or cron job.
- Expand RSS sources to cover more mountain biking news globally.
- Enhance tweet formatting and engagement strategies.

## License
MIT License

## Contributing
Feel free to open issues or submit pull requests to improve the bot!

---

Happy tweeting! 🚵‍♂️🔥

