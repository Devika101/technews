"""
Authentication Component for Tech News App
"""
import streamlit as st
import requests
import json
import os
from firebase_config import initialize_firebase, verify_token, get_user_data, save_user_data

# Firebase Web API Key (for client-side auth)
try:
    FIREBASE_WEB_API_KEY = st.secrets.get("FIREBASE_WEB_API_KEY", os.getenv("FIREBASE_WEB_API_KEY"))
except:
    FIREBASE_WEB_API_KEY = os.getenv("FIREBASE_WEB_API_KEY")

def show_login_form():
    """Display login form"""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="color: #8b5cf6; text-shadow: 0 0 10px rgba(139, 92, 246, 0.3);">🔐 Access Portal</h2>
        <p style="color: #6b7280;">Enter the digital realm</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("login_form"):
        email = st.text_input("📧 Email", placeholder="your@email.com")
        password = st.text_input("🔑 Password", type="password", placeholder="••••••••")
        
        col1, col2 = st.columns(2)
        with col1:
            login_clicked = st.form_submit_button("🚀 Login", use_container_width=True)
        with col2:
            register_clicked = st.form_submit_button("✨ Register", use_container_width=True)
    
    return email, password, login_clicked, register_clicked

def authenticate_user(email, password, is_register=False):
    """Authenticate user with Firebase"""
    if not FIREBASE_WEB_API_KEY:
        st.error("Firebase Web API key not configured")
        return None
    
    # Firebase Auth REST API endpoint
    auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
    
    if is_register:
        auth_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_WEB_API_KEY}"
    
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    
    try:
        response = requests.post(auth_url, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'uid': data['localId'],
                'email': data['email'],
                'id_token': data['idToken'],
                'refresh_token': data['refreshToken']
            }
        else:
            error_data = response.json()
            st.error(f"Authentication failed: {error_data.get('error', {}).get('message', 'Unknown error')}")
            return None
    except Exception as e:
        st.error(f"Authentication error: {e}")
        return None

def show_user_profile(user_data):
    """Display user profile in sidebar"""
    with st.sidebar:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8f4ff, #e8d5f2); 
                    padding: 1rem; border-radius: 10px; 
                    border: 1px solid #8b5cf6; margin-bottom: 1rem;">
            <h4 style="color: #8b5cf6; margin: 0;">👤 User Profile</h4>
            <p style="color: #6b7280; margin: 0.5rem 0;">{}</p>
        </div>
        """.format(user_data.get('email', 'Unknown')), unsafe_allow_html=True)
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.clear()
            st.rerun()

def check_authentication():
    """Check if user is authenticated"""
    if 'user' not in st.session_state:
        return False
    
    # Verify token is still valid
    try:
        decoded_token = verify_token(st.session_state['user']['id_token'])
        if decoded_token:
            return True
    except:
        pass
    
    # Clear invalid session
    st.session_state.clear()
    return False

def require_auth():
    """Decorator to require authentication"""
    if not check_authentication():
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2 style="color: #ec4899;">🔒 Authentication Required</h2>
            <p style="color: #6b7280;">Please log in to access the tech news portal</p>
        </div>
        """, unsafe_allow_html=True)
        return False
    return True
