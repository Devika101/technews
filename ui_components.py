"""
Futuristic UI Components for Tech News App
"""
import streamlit as st

def apply_futuristic_theme():
    """Apply futuristic cyberpunk theme"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #f8f4ff 0%, #e8d5f2 50%, #d4b3e8 100%);
        color: #4a4a4a;
        font-family: 'Exo 2', sans-serif;
    }
    
    /* Main Container */
    .main .block-container {
        padding: 2rem 1rem;
        max-width: 1200px;
    }
    
    /* Headers */
    h1 {
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        color: #8b5cf6;
        text-shadow: 0 0 20px rgba(139, 92, 246, 0.3);
        text-align: center;
        margin-bottom: 2rem;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    h2 {
        font-family: 'Orbitron', monospace;
        color: #8b5cf6;
        text-shadow: 0 0 10px rgba(139, 92, 246, 0.3);
        border-bottom: 2px solid #8b5cf6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    
    h3 {
        font-family: 'Orbitron', monospace;
        color: #ec4899;
        text-shadow: 0 0 5px rgba(236, 72, 153, 0.3);
    }
    
    /* Glow Animation */
    @keyframes glow {
        from { text-shadow: 0 0 20px rgba(139, 92, 246, 0.3); }
        to { text-shadow: 0 0 30px rgba(139, 92, 246, 0.5), 0 0 40px rgba(139, 92, 246, 0.3); }
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #8b5cf6, #a855f7);
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        font-family: 'Orbitron', monospace;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #a855f7, #8b5cf6);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
    }
    
    /* Primary Button */
    .stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #ec4899, #f472b6);
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3);
    }
    
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(45deg, #f472b6, #ec4899);
        box-shadow: 0 6px 20px rgba(236, 72, 153, 0.5);
    }
    
    /* Cards */
    .news-card {
        background: linear-gradient(135deg, rgba(248, 244, 255, 0.8), rgba(232, 213, 242, 0.8));
        border: 1px solid #8b5cf6;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(139, 92, 246, 0.1);
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .news-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(139, 92, 246, 0.2);
        border-color: #8b5cf6;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f4ff, #e8d5f2);
        border-right: 2px solid #8b5cf6;
    }
    
    /* Input Fields */
    .stTextInput > div > div > input {
        background: rgba(248, 244, 255, 0.8);
        border: 1px solid #8b5cf6;
        border-radius: 8px;
        color: #000000;
        padding: 0.5rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8b5cf6;
        box-shadow: 0 0 10px rgba(139, 92, 246, 0.3);
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background: rgba(248, 244, 255, 0.8);
        border: 1px solid #8b5cf6;
        border-radius: 8px;
    }
    
    /* Checkbox */
    .stCheckbox > label {
        color: #000000;
        font-weight: 600;
    }
    
    /* Form Labels */
    .stTextInput > label {
        color: #000000;
        font-weight: 600;
    }
    
    /* Placeholder text */
    .stTextInput > div > div > input::placeholder {
        color: #6b7280;
    }
    
    /* Spinner */
    .stSpinner {
        color: #8b5cf6;
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1), rgba(168, 85, 247, 0.1));
        border: 1px solid #8b5cf6;
        border-radius: 8px;
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(236, 72, 153, 0.1), rgba(244, 114, 182, 0.1));
        border: 1px solid #ec4899;
        border-radius: 8px;
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(245, 158, 11, 0.1));
        border: 1px solid #fbbf24;
        border-radius: 8px;
    }
    
    /* Images */
    .stImage {
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(139, 92, 246, 0.2);
    }
    
    /* Links */
    a {
        color: #8b5cf6;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    a:hover {
        color: #a855f7;
        text-shadow: 0 0 5px rgba(139, 92, 246, 0.3);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #8b5cf6, transparent);
        margin: 2rem 0;
    }
    
    /* Footer */
    .stCaption {
        color: #6b7280;
        text-align: center;
        font-size: 0.9rem;
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f8f4ff;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #8b5cf6;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #a855f7;
    }
    </style>
    """, unsafe_allow_html=True)

def create_cyberpunk_header():
    """Create elegant header with purple/pink theme"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; margin-bottom: 2rem;">
        <h1 style="font-family: 'Orbitron', monospace; font-weight: 900; 
                   color: #8b5cf6; text-shadow: 0 0 20px rgba(139, 92, 246, 0.3); 
                   margin-bottom: 0.5rem; animation: glow 2s ease-in-out infinite alternate;">
            📰 TECH DAILY
        </h1>
        <p style="color: #6b7280; font-size: 1.2rem; margin: 0;">
            AI-Powered News Portal • Digital Information Hub
        </p>
        <div style="margin-top: 1rem; height: 2px; 
                    background: linear-gradient(90deg, transparent, #8b5cf6, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)

def create_news_card(article, index):
    """Create elegant news card with purple/pink theme"""
    st.markdown(f"""
    <div class="news-card">
        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
            <span style="background: linear-gradient(45deg, #8b5cf6, #a855f7); 
                        color: #ffffff; padding: 0.3rem 0.8rem; border-radius: 20px; 
                        font-weight: 700; font-family: 'Orbitron', monospace; 
                        font-size: 0.9rem; margin-right: 1rem;">
                #{index}
            </span>
            <h3 style="margin: 0; color: #8b5cf6; font-family: 'Orbitron', monospace;">
                {article.get('title', 'No Title')}
            </h3>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_loading_animation():
    """Create elegant loading animation"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <div style="display: inline-block; width: 40px; height: 40px; 
                    border: 3px solid #8b5cf6; border-top: 3px solid transparent; 
                    border-radius: 50%; animation: spin 1s linear infinite; 
                    margin-bottom: 1rem;"></div>
        <p style="color: #8b5cf6; font-family: 'Orbitron', monospace; 
                 text-shadow: 0 0 10px rgba(139, 92, 246, 0.3);">PROCESSING DATA...</p>
    </div>
    
    <style>
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    """, unsafe_allow_html=True)

def create_footer():
    """Create elegant footer"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem; margin-top: 3rem; 
                border-top: 2px solid #8b5cf6; background: linear-gradient(135deg, 
                rgba(248, 244, 255, 0.5), rgba(232, 213, 242, 0.5));">
        <p style="color: #6b7280; margin: 0; font-size: 0.9rem;">
            ⚡ Powered by AI • 🔮 Future Technology • 🌐 Global Network
        </p>
        <p style="color: #8b5cf6; margin: 0.5rem 0 0 0; font-family: 'Orbitron', monospace;">
            TECH DAILY v2.0
        </p>
    </div>
    """, unsafe_allow_html=True)
