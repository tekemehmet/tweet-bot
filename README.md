# MTB News Twitter Bot 🚵‍♂️

A sophisticated Twitter bot that automatically fetches, summarizes, and shares mountain biking news in Turkish. The bot uses OpenAI's GPT-4 model for intelligent summarization and ensures engaging, concise content delivery while maintaining Twitter's character limits.

## 🌟 Features

- **Automated News Aggregation**: Fetches latest mountain biking news from curated RSS feeds
- **Smart Summarization**: Uses GPT-4 to create engaging, two-sentence summaries in Turkish
- **Character-Limit Optimization**: Automatically ensures tweets fit within Twitter's 280-character limit
- **Duplicate Prevention**: Maintains a history of posted articles to avoid repetition
- **Source Attribution**: Automatically posts source links as reply tweets
- **Hashtag Integration**: Includes relevant MTB hashtags for better visibility

## 🛠️ Technical Stack

- **Python 3.x**
- **APIs and Services**:
  - Twitter API (via Tweepy)
  - OpenAI GPT-4 API
- **Key Libraries**:
  - `tweepy`: Twitter API integration
  - `openai`: GPT-4 API integration
  - `python-dotenv`: Environment variable management

## 📋 Prerequisites

1. Python 3.x installed
2. Twitter Developer Account with Elevated access
3. OpenAI API account and key
4. Basic understanding of command line operations

## 🚀 Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/tekemehmet/tweet-bot
   ```

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   TWITTER_CONSUMER_API_KEY=your_consumer_key
   TWITTER_CONSUMER_API_SECRET=your_consumer_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_SECRET=your_access_secret
   OPENAI_API_KEY=your_openai_api_key
   ```

## 🎯 Usage

1. **Run the Bot**
   ```sh
   python main.py
   ```

2. **Monitor Output**
   - The bot will print status messages to the console
   - Check your Twitter profile for posted tweets
   - Review `posted_news.txt` for tracking

## 📁 Project Structure

```
mtb-news-bot/
├── main.py           # Main execution script
├── auth.py          # API authentication handling
├── summarizer.py    # News summarization logic
├── rss_fetcher.py   # RSS feed processing
├── utils.py         # Utility functions
├── posted_news.txt  # History tracking
├── requirements.txt # Dependencies
└── .env            # Configuration
```

## 🔧 Configuration

The bot can be customized through various parameters:
- Summary length (default: 250 characters)
- Language settings (currently Turkish)
- Hashtag configuration
- RSS feed sources

## 🚧 Future Enhancements

1. **Cloud Integration**
   - Migration to cloud hosting (e.g., Google Cloud)
   - Database integration for better state management
   - Automated scheduling with cloud functions

2. **Feature Expansion**
   - Multi-language support
   - Image processing from news articles
   - Engagement analytics tracking
   - Interactive user commands

3. **Content Improvements**
   - Dynamic hashtag optimization
   - Sentiment analysis for content filtering
   - Advanced duplicate detection

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

Common issues and solutions:
1. **API Authentication Errors**: Verify your API keys in `.env`
2. **Rate Limiting**: Ensure compliance with Twitter API limits
3. **Character Limit Exceeded**: Check summary length configurations

## 📞 Support

For support, please:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include relevant error messages and logs

---

Happy MTB News Tweeting! 🚵‍♂️🌟

