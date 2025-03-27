import streamlit as st
import hashlib
import json
import os

# Initialize session state for user management
if 'users' not in st.session_state:
    st.session_state.users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password):
    if username in st.session_state.users:
        return False, "Username already exists"
    
    st.session_state.users[username] = {
        'password': hash_password(password),
        'name': username
    }
    return True, "Signup successful"

def login(username, password):
    if username not in st.session_state.users:
        return False, "User not found"
    
    if st.session_state.users[username]['password'] != hash_password(password):
        return False, "Incorrect password"
    
    st.session_state.current_user = username
    return True, "Login successful"

def logout():
    if 'current_user' in st.session_state:
        del st.session_state.current_user
    return True, "Logged out successfully" 