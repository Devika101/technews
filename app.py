import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from auth_component import show_login_form, authenticate_user, show_user_profile, require_auth
from ui_components import apply_futuristic_theme, create_cyberpunk_header, create_news_card, create_loading_animation, create_footer

# Load environment variables
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Streamlit Page Config
st.set_page_config(
    page_title="Tech Daily", 
    page_icon="📰", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply futuristic theme
apply_futuristic_theme()

# Authentication Check
if 'user' not in st.session_state:
    # Show login form
    create_cyberpunk_header()
    email, password, login_clicked, register_clicked = show_login_form()
    
    if login_clicked or register_clicked:
        if email and password:
            user_data = authenticate_user(email, password, register_clicked)
            if user_data:
                st.session_state['user'] = user_data
                st.success("🚀 Authentication successful! Welcome to the digital realm.")
                st.rerun()
        else:
            st.error("Please enter both email and password.")
    
    st.stop()

# User is authenticated - show main app
show_user_profile(st.session_state['user'])
create_cyberpunk_header()

# Function to fetch news
@st.cache_data(ttl=86400)  # Cache data for 24 hours
def fetch_news():
    if not NEWS_API_KEY:
        st.error("⚠️ NEWS_API_KEY not found. Please add it to your .env file.")
        return []
    
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={NEWS_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "ok":
                return data.get("articles", [])
            else:
                st.error(f"NewsAPI error: {data.get('message', 'Unknown error')}")
                return []
        elif response.status_code == 401:
            st.error("❌ Invalid NewsAPI key. Please check your API key.")
            return []
        elif response.status_code == 429:
            st.error("⏰ API rate limit exceeded. Please try again later.")
            return []
        else:
            st.error(f"Failed to fetch news. Status code: {response.status_code}")
            return []
    except requests.exceptions.Timeout:
        st.error("⏱️ Request timed out. Please check your internet connection.")
        return []
    except requests.exceptions.ConnectionError:
        st.error("🌐 Connection error. Please check your internet connection.")
        return []
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        return []

# Function to summarize news using OpenRouter
def summarize_with_openrouter(title, description, debug_mode=False):
    if not description:
        return "No description available."

    if not OPENROUTER_API_KEY:
        return description  # fallback if API key missing
    
    # Debug mode - show API key status
    if debug_mode:
        st.sidebar.write(f"OpenRouter API Key: {'✅ Set' if OPENROUTER_API_KEY else '❌ Missing'}")
        st.sidebar.write(f"Title length: {len(title)}")
        st.sidebar.write(f"Description length: {len(description)}")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an expert AI news summarizer. Summarize briefly in 2-3 sentences."},
            {"role": "user", "content": f"Title: {title}\n\nDescription: {description}\n\nSummarize this for a tech news digest."}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers, timeout=30)
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"].strip()
            else:
                return description
        elif response.status_code == 401:
            st.warning("⚠️ Invalid OpenRouter API key. Using original description.")
            return description
        elif response.status_code == 429:
            st.warning("⏰ OpenRouter rate limit exceeded. Using original description.")
            return description
        elif response.status_code == 400:
            try:
                error_data = response.json()
                error_msg = error_data.get("error", {}).get("message", "Bad request")
                st.warning(f"OpenRouter API error: {error_msg}. Using original description.")
            except:
                st.warning("OpenRouter API error (400): Bad request. Using original description.")
            return description
        else:
            try:
                error_data = response.json()
                error_msg = error_data.get("error", {}).get("message", f"Status {response.status_code}")
                st.warning(f"OpenRouter API error: {error_msg}. Using original description.")
            except:
                st.warning(f"OpenRouter API error (status {response.status_code}). Using original description.")
            return description
    except requests.exceptions.Timeout:
        st.warning("⏱️ OpenRouter request timed out. Using original description.")
        return description
    except requests.exceptions.ConnectionError:
        st.warning("🌐 OpenRouter connection error. Using original description.")
        return description
    except Exception as e:
        st.warning(f"OpenRouter summarization failed: {e}. Using original description.")
        return description

# Remove debug mode

# Fetch and display news
articles = fetch_news()

if articles:
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #8b5cf6; font-family: 'Orbitron', monospace;">
            📡 DATA STREAM ACTIVE
        </h2>
        <p style="color: #6b7280;">Latest tech news from the digital network</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    for i, article in enumerate(articles[:15], 1):
        # Create elegant news card
        st.markdown(f"""
        <div class="news-card">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="background: linear-gradient(45deg, #8b5cf6, #a855f7); 
                            color: #ffffff; padding: 0.3rem 0.8rem; border-radius: 20px; 
                            font-weight: 700; font-family: 'Orbitron', monospace; 
                            font-size: 0.9rem; margin-right: 1rem;">
                    #{i}
                </span>
                <h3 style="margin: 0; color: #8b5cf6; font-family: 'Orbitron', monospace;">
                    {article.get('title', 'No Title')}
                </h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display image if available
        if article.get("urlToImage"):
            try:
                st.image(article["urlToImage"], width="stretch", caption="📸 Article Image")
            except Exception:
                st.info("🖼️ Image could not be loaded")
        
        # Show publication info
        if article.get("publishedAt"):
            pub_date = datetime.fromisoformat(article["publishedAt"].replace('Z', '+00:00'))
            st.markdown(f"""
            <div style="background: rgba(248, 244, 255, 0.5); padding: 0.5rem 1rem; 
                        border-radius: 8px; border-left: 3px solid #8b5cf6; margin: 1rem 0;">
                <p style="color: #6b7280; margin: 0; font-size: 0.9rem;">
                    📅 Published: {pub_date.strftime('%Y-%m-%d %H:%M')} | 
                    📡 Source: {article.get('source', {}).get('name', 'Unknown')}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # Summarize with loading indicator
        with st.spinner("🤖 AI is analyzing article data..."):
            summary = summarize_with_openrouter(article["title"], article.get("description", ""), False)
        
        # Display summary in elegant style
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(168, 85, 247, 0.1));
                    border: 1px solid #8b5cf6; border-radius: 10px; padding: 1rem; margin: 1rem 0;">
            <h4 style="color: #8b5cf6; margin: 0 0 0.5rem 0; font-family: 'Orbitron', monospace;">
                🤖 AI ANALYSIS
            </h4>
            <p style="color: #4a4a4a; margin: 0; line-height: 1.6;">
                {summary}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Link to full article
        if article.get("url"):
            st.markdown(f"""
            <div style="text-align: center; margin: 1rem 0;">
                <a href="{article['url']}" target="_blank" 
                   style="display: inline-block; background: linear-gradient(45deg, #ec4899, #f472b6);
                          color: #ffffff; padding: 0.5rem 1.5rem; border-radius: 25px; 
                          text-decoration: none; font-weight: 600; font-family: 'Orbitron', monospace;
                          transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3);">
                    🔗 ACCESS FULL ARTICLE
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
else:
    st.markdown("""
    <div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, 
                rgba(236, 72, 153, 0.1), rgba(244, 114, 182, 0.1)); 
                border: 1px solid #ec4899; border-radius: 15px; margin: 2rem 0;">
        <h3 style="color: #ec4899; font-family: 'Orbitron', monospace;">
            ⚠️ DATA STREAM INTERRUPTED
        </h3>
        <p style="color: #6b7280;">No tech news available. Check your API key and internet connection.</p>
    </div>
    """, unsafe_allow_html=True)

# Elegant Footer
create_footer()
st.markdown(f"""
<div style="text-align: center; margin-top: 2rem; padding: 1rem; 
            background: rgba(248, 244, 255, 0.3); border-radius: 10px; 
            border: 1px solid #8b5cf6;">
    <p style="color: #6b7280; margin: 0; font-size: 0.9rem;">
        Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </p>
</div>
""", unsafe_allow_html=True)
