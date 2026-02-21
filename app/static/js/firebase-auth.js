// Firebase Configuration
// Replace these values with your Firebase project credentials from Firebase Console

const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Firebase Auth instances
const auth = firebase.auth();
const googleProvider = new firebase.auth.GoogleAuthProvider();
const githubProvider = new firebase.auth.GitHubAuthProvider();

// Current user state
let currentUser = null;

// Listen for auth state changes
auth.onAuthStateChanged((user) => {
    currentUser = user;
    updateAuthUI(user);

    // Dispatch custom event for other parts of the app
    window.dispatchEvent(new CustomEvent('authStateChange', { detail: { user } }));
});

// Sign in with email/password
async function signInWithEmail(email, password) {
    try {
        const result = await auth.signInWithEmailAndPassword(email, password);
        return { success: true, user: result.user };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// Sign in with Google
async function signInWithGoogle() {
    try {
        const result = await auth.signInWithPopup(googleProvider);
        return { success: true, user: result.user };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// Sign in with GitHub
async function signInWithGitHub() {
    try {
        const result = await auth.signInWithPopup(githubProvider);
        return { success: true, user: result.user };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// Register with email/password
async function registerWithEmail(email, password, displayName) {
    try {
        const result = await auth.createUserWithEmailAndPassword(email, password);
        if (displayName) {
            await result.user.updateProfile({ displayName: displayName });
        }
        return { success: true, user: result.user };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// Sign out
async function signOut() {
    try {
        await auth.signOut();
        return { success: true };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

// Update UI based on auth state
function updateAuthUI(user) {
    const authButtons = document.getElementById('auth-buttons');
    const userProfile = document.getElementById('user-profile');
    const userAvatar = document.getElementById('user-avatar');
    const userName = document.getElementById('user-name');
    const userLevel = document.getElementById('user-level');

    // Header elements
    const headerLoginBtn = document.getElementById('header-login-btn');
    const headerUserProfile = document.getElementById('header-user-profile');
    const headerUserAvatar = document.getElementById('header-user-avatar');

    if (user) {
        // User is signed in
        if (authButtons) authButtons.classList.add('hidden');
        if (headerLoginBtn) headerLoginBtn.classList.add('hidden');
        if (userProfile) {
            userProfile.classList.remove('hidden');
            if (userName) userName.textContent = user.displayName || user.email.split('@')[0];
            if (userAvatar) {
                if (user.photoURL) {
                    userAvatar.src = user.photoURL;
                } else {
                    // Generate initials avatar
                    const initials = (user.displayName || user.email).charAt(0).toUpperCase();
                    userAvatar.outerHTML = `<div class="w-8 h-8 rounded-full bg-gradient-to-tr from-neon-blue to-neon-pink flex items-center justify-center text-xs font-bold">${initials}</div>`;
                }
            }
        }
        if (headerUserProfile) {
            headerUserProfile.classList.remove('hidden');
            if (headerUserAvatar && user.photoURL) {
                headerUserAvatar.src = user.photoURL;
            }
        }
    } else {
        // User is signed out
        if (authButtons) authButtons.classList.remove('hidden');
        if (headerLoginBtn) headerLoginBtn.classList.remove('hidden');
        if (userProfile) userProfile.classList.add('hidden');
        if (headerUserProfile) headerUserProfile.classList.add('hidden');
    }
}

// Check if user is authenticated
function isAuthenticated() {
    return currentUser !== null;
}

// Get current user
function getCurrentUser() {
    return currentUser;
}

// Protect a route - call this on page load to require authentication
function requireAuth(callback) {
    auth.onAuthStateChanged((user) => {
        if (!user) {
            // Not logged in, redirect to login
            window.location.href = '/login';
        } else if (callback) {
            callback(user);
        }
    });
}

// Check if user is logged in and show content accordingly
function checkAuthForFeature() {
    return new Promise((resolve) => {
        auth.onAuthStateChanged((user) => {
            resolve(user);
        });
    });
}
