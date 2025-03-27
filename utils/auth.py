import streamlit as st
import hashlib
import json
import os
import requests
from .config import AUTH_ENDPOINT

# Initialize session state for user management
if 'users' not in st.session_state:
    st.session_state.users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password):
    try:
        response = requests.post(
            f"{AUTH_ENDPOINT}/signup",
            json={"username": username, "password": hash_password(password)}
        )
        if response.status_code == 200:
            return True, "Signup successful"
        return False, response.json().get("detail", "Signup failed")
    except Exception as e:
        return False, f"Error during signup: {str(e)}"

def login(username, password):
    try:
        response = requests.post(
            f"{AUTH_ENDPOINT}/login",
            data={"username": username, "password": password}
        )
        if response.status_code == 200:
            st.session_state.current_user = username
            st.session_state.token = response.json().get("access_token")
            return True, "Login successful"
        return False, response.json().get("detail", "Login failed")
    except Exception as e:
        return False, f"Error during login: {str(e)}"

def logout():
    if 'current_user' in st.session_state:
        del st.session_state.current_user
    if 'token' in st.session_state:
        del st.session_state.token
    return True, "Logged out successfully" 