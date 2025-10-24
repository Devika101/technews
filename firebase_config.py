"""
Firebase Configuration and Authentication
"""
import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, firestore
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Firebase Admin SDK
def initialize_firebase():
    """Initialize Firebase Admin SDK"""
    if not firebase_admin._apps:
        # Get Firebase service account key from environment
        firebase_key = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")
        
        if not firebase_key:
            st.error("Firebase service account key not found. Please set FIREBASE_SERVICE_ACCOUNT_KEY in your .env file")
            return False
        
        try:
            # Parse the JSON key
            service_account_info = json.loads(firebase_key)
            cred = credentials.Certificate(service_account_info)
            firebase_admin.initialize_app(cred)
            return True
        except Exception as e:
            st.error(f"Failed to initialize Firebase: {e}")
            return False
    return True

# Authentication functions
def verify_token(token):
    """Verify Firebase ID token"""
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        st.error(f"Token verification failed: {e}")
        return None

def get_user_data(uid):
    """Get user data from Firestore"""
    try:
        db = firestore.client()
        user_ref = db.collection('users').document(uid)
        user_doc = user_ref.get()
        
        if user_doc.exists:
            return user_doc.to_dict()
        return None
    except Exception as e:
        st.error(f"Failed to get user data: {e}")
        return None

def save_user_data(uid, user_data):
    """Save user data to Firestore"""
    try:
        db = firestore.client()
        user_ref = db.collection('users').document(uid)
        user_ref.set(user_data, merge=True)
        return True
    except Exception as e:
        st.error(f"Failed to save user data: {e}")
        return False


