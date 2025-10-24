# 🔥 Firebase Authentication Setup Guide

This guide will help you set up Firebase authentication for your Tech Daily app.

## Step 1: Create Firebase Project

1. **Go to Firebase Console**
   - Visit [https://console.firebase.google.com/](https://console.firebase.google.com/)
   - Click "Create a project" or "Add project"

2. **Project Setup**
   - Enter project name: `tech-daily-app` (or your preferred name)
   - Enable Google Analytics (optional)
   - Click "Create project"

## Step 2: Enable Authentication

1. **Navigate to Authentication**
   - In the Firebase console, click "Authentication" in the left sidebar
   - Click "Get started"

2. **Enable Email/Password Authentication**
   - Click on "Sign-in method" tab
   - Click on "Email/Password"
   - Enable "Email/Password" provider
   - Click "Save"

## Step 3: Get Firebase Configuration

1. **Get Web API Key**
   - Go to Project Settings (gear icon)
   - Scroll down to "Your apps" section
   - Click "Add app" → Web app (</>) icon
   - Register app with name: `tech-daily-web`
   - Copy the `apiKey` value

2. **Get Service Account Key**
   - Go to Project Settings → Service accounts tab
   - Click "Generate new private key"
   - Download the JSON file
   - **Keep this file secure!**

## Step 4: Configure Environment Variables

Create or update your `.env` file:

```env
# Existing API keys
NEWS_API_KEY=your_news_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Firebase Configuration
FIREBASE_WEB_API_KEY=your_firebase_web_api_key_here
FIREBASE_SERVICE_ACCOUNT_KEY={"type":"service_account","project_id":"your-project-id",...}
```

**Important:** The `FIREBASE_SERVICE_ACCOUNT_KEY` should be the entire JSON content as a single line.

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 6: Test the Setup

1. **Run the app:**
   ```bash
   streamlit run app.py
   ```

2. **Test authentication:**
   - Try registering a new account
   - Try logging in with existing credentials
   - Check if the user profile appears in the sidebar

## Step 7: Firestore Database (Optional)

For advanced user data storage:

1. **Enable Firestore**
   - Go to "Firestore Database" in Firebase console
   - Click "Create database"
   - Choose "Start in test mode"
   - Select a location

2. **Security Rules (Production)**
   ```javascript
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /users/{userId} {
         allow read, write: if request.auth != null && request.auth.uid == userId;
       }
     }
   }
   ```

## Troubleshooting

### Common Issues:

1. **"Firebase Web API key not configured"**
   - Check your `.env` file has `FIREBASE_WEB_API_KEY`
   - Restart the app after adding the key

2. **"Authentication failed"**
   - Verify the email/password is correct
   - Check Firebase console for user accounts
   - Ensure Email/Password auth is enabled

3. **"Service account key error"**
   - Verify the JSON is properly formatted
   - Check the key has the correct permissions
   - Ensure no extra spaces or line breaks in the JSON

### Security Best Practices:

1. **Never commit `.env` files to version control**
2. **Use environment variables in production**
3. **Rotate API keys regularly**
4. **Set up proper Firestore security rules**
5. **Monitor authentication logs in Firebase console**

## Production Deployment

For production deployment:

1. **Set up proper security rules**
2. **Use environment variables instead of `.env`**
3. **Enable Firebase App Check for additional security**
4. **Set up monitoring and alerts**
5. **Configure custom domain (optional)**

## Support

- Firebase Documentation: [https://firebase.google.com/docs](https://firebase.google.com/docs)
- Streamlit Authentication: [https://docs.streamlit.io/library/advanced-features/authentication](https://docs.streamlit.io/library/advanced-features/authentication)

Your futuristic tech news app is now ready with secure authentication! 🚀


