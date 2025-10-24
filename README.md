# Tech Daily - AI Powered Tech News Digest

A Streamlit app that fetches the latest tech news and provides AI-powered summaries using OpenRouter.
Check it out:https://technews-gqcimpwrnelqibxwicrak5.streamlit.app/

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get API keys:**
   - **NewsAPI**: Get your free API key from [newsapi.org](https://newsapi.org/register)
   - **OpenRouter**: Get your API key from [openrouter.ai](https://openrouter.ai/keys)

3. **Create environment file:**
   - Copy `.env.example` to `.env`
   - Fill in your API keys:
   ```
   NEWS_API_KEY=your_news_api_key_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Features

- 📰 Fetches latest tech news from NewsAPI
- 🤖 AI-powered article summaries using OpenRouter
- 🖼️ Displays article images
- ⚡ 24-hour caching for better performance
- 📱 Responsive design

## Notes

- The app caches news data for 24 hours to avoid hitting API limits
- If OpenRouter API key is missing, it will show original descriptions
- Make sure you have a stable internet connection for fetching news
