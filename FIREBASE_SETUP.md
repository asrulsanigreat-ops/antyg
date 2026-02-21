# Firebase Authentication Setup Guide

This guide will help you set up Firebase Authentication for your Nebula Learning App.

## Prerequisites

1. A Google account to access Firebase Console
2. Your app downloaded the Firebase extension

## Step 1: Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project" and follow the steps
3. Enter your project name (e.g., "nebula-learning-app")
4. Disable Google Analytics (optional, for simpler setup)
5. Click "Create project"

## Step 2: Register Your App

1. In Firebase Console, click the web icon (</>) to add a web app
2. Register your app (e.g., "Nebula Web App")
3. Copy the Firebase config object provided

## Step 3: Configure Authentication

1. In Firebase Console, go to **Authentication** → **Get Started**
2. Enable the following sign-in methods:
   - **Email/Password**: Enable both "Email/Password" and "Email link (passwordless sign-in)"
   - **Google**: Enable and add your email to the authorized domains
   - **GitHub**: Enable, create a GitHub OAuth app, and add the credentials

## Step 4: Update Firebase Config

Open `app/static/js/firebase-auth.js` and replace the placeholder values with your actual Firebase credentials:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};
```

### Where to find these values:
- In Firebase Console → Project Settings → General tab
- Scroll down to "Your apps" and click on your web app

## Step 5: Configure Authorized Domains

1. In Firebase Console → Authentication → Settings → Authorized domains
2. Add your local domain (e.g., `localhost`, `127.0.0.1`)
3. Add your production domain if deploying

## Step 6: Enable GitHub OAuth (Optional)

1. Go to [GitHub Developer Settings](https://github.com/settings/developers)
2. Click "New OAuth App"
3. Fill in:
   - Application name: "Nebula Learning"
   - Homepage URL: `http://localhost:8000`
   - Authorization callback URL: Copy from Firebase Console → Authentication → GitHub
4. Copy Client ID and Client Secret to Firebase Console

## Testing the App

1. Start your FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

2. Open http://localhost:8000/login
3. Try signing in with:
   - Email/Password (register a new account)
   - Google (sign in with Google)
   - GitHub (sign in with GitHub)

## Security Rules

When deploying to production, consider setting up security rules in Firebase:

```
// Allow only authenticated users
allow read, write: if request.auth != null;
```

## Troubleshooting

- **CORS errors**: Make sure your domain is in authorized domains
- **Google sign-in not working**: Verify the OAuth consent screen is configured
- **Email/password not working**: Make sure "Email/Password" is enabled in Firebase Console
- **Session not persisting**: Check browser cookies are not blocked
