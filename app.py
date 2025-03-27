import streamlit as st
from utils.auth import login, signup, logout
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="AI Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Main container styles */
    .main {
        background-color: #1E1E1E;
        color: #FFFFFF;
        padding: 2rem;
    }
    
    /* Card styles */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #2D2D2D;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Button styles */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        margin-top: 1em;
        background-color: #0096FF;
        color: white;
        border: none;
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #007ACC;
    }
    
    /* Input field styles */
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #4A4A4A;
        background-color: #2D2D2D;
        color: white;
    }
    
    /* Header styles */
    h1, h2, h3 {
        color: #0096FF !important;
    }
    
    /* Center main title */
    .main-title {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Link styles */
    a {
        color: #0096FF !important;
    }
    
    /* Sidebar styles */
    .css-1d391kg {
        background-color: #2D2D2D;
        padding-top: 2rem;
    }
    
    /* Sidebar auth container */
    .sidebar-auth {
        background: linear-gradient(145deg, #2D2D2D, #363636);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    .sidebar-auth h1 {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 1.5rem !important;
        margin-bottom: 1rem !important;
        background: linear-gradient(90deg, #0096FF, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Sidebar button container */
    .sidebar-buttons {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.5rem;
    }

    .sidebar-buttons button {
        background: linear-gradient(145deg, #2D2D2D, #363636) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: #0096FF !important;
        padding: 0.75rem !important;
        border-radius: 8px !important;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
        width: 100%;
        height: auto !important;
        margin-top: 0 !important;
    }

    .sidebar-buttons button:hover {
        transform: translateY(-2px);
        border-color: #0096FF !important;
        box-shadow: 0 4px 15px rgba(0, 150, 255, 0.2);
        background: linear-gradient(90deg, #0096FF, #00D4FF) !important;
        color: white !important;
    }

    .sidebar-buttons button::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent, rgba(0, 150, 255, 0.1), transparent);
        transform: translateX(-100%);
        transition: 0.5s;
    }

    .sidebar-buttons button:hover::before {
        transform: translateX(100%);
    }

    /* Auth container styles */
    .auth-container {
        background: linear-gradient(145deg, #2D2D2D, #363636);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    .auth-title {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .auth-title h1 {
        font-size: 1.5rem !important;
        margin: 0 !important;
        background: linear-gradient(90deg, #0096FF, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .auth-buttons {
        display: flex;
        gap: 0.5rem;
    }
    
    .auth-buttons button {
        flex: 1;
        background: linear-gradient(90deg, #0096FF, #00D4FF);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .auth-buttons button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 150, 255, 0.4);
    }
    
    /* Card container styles */
    .service-card {
        background: linear-gradient(145deg, #2D2D2D, #363636);
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .service-card:before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent, rgba(0, 150, 255, 0.1), transparent);
        transform: translateX(-100%);
        transition: 0.5s;
    }
    
    .service-card:hover {
        transform: translateY(-5px);
        border-color: #0096FF;
        box-shadow: 0 12px 40px 0 rgba(0, 150, 255, 0.3);
    }
    
    .service-card:hover:before {
        transform: translateX(100%);
    }
    
    .service-card h3 {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .service-card p {
        color: #B0B0B0;
        font-size: 1.1rem;
        line-height: 1.5;
    }
    
    .service-card-icon {
        font-size: 2rem;
        margin-right: 0.5rem;
    }

    /* Auth form styles */
    .auth-form {
        background: linear-gradient(145deg, #2D2D2D, #363636);
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 2rem;
        max-width: 400px;
        margin-left: auto;
        margin-right: auto;
    }

    .auth-form .stTextInput>div>div>input {
        background: rgba(45, 45, 45, 0.9);
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        height: 3em;
        transition: all 0.3s ease;
    }

    .auth-form .stTextInput>div>div>input:focus {
        border-color: #0096FF;
        box-shadow: 0 0 0 2px rgba(0, 150, 255, 0.2);
    }

    .auth-form .stButton>button {
        background: linear-gradient(90deg, #0096FF, #00D4FF);
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 1.5rem;
    }

    .auth-form .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 150, 255, 0.4);
    }

    .auth-form h3 {
        text-align: center;
        margin-bottom: 1.5rem;
        background: linear-gradient(90deg, #0096FF, #00D4FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.75rem;
    }

    /* Chatbot interface styles */
    .chat-header {
        background: linear-gradient(90deg, #0096FF, #00D4FF);
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0, 150, 255, 0.2);
        text-align: center;
    }

    .chat-header h1 {
        color: white !important;
        margin: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        font-size: 2rem;
    }

    .chat-header p {
        color: rgba(255, 255, 255, 0.9);
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
    }

    /* Message styles */
    .stChatMessage {
        background: linear-gradient(145deg, rgba(45, 45, 45, 0.6), rgba(54, 54, 54, 0.6)) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 15px !important;
        padding: 1rem !important;
        margin-bottom: 1rem !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
    }

    .stChatMessage:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 150, 255, 0.1);
    }

    /* Chat input styles */
    .stChatInputContainer {
        padding-top: 1rem !important;
        margin-top: 1rem !important;
        border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
    }

    .stChatInputContainer textarea {
        background: rgba(45, 45, 45, 0.9) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: white !important;
        padding: 0.75rem !important;
        transition: all 0.3s ease !important;
    }

    .stChatInputContainer textarea:focus {
        border-color: #0096FF !important;
        box-shadow: 0 0 0 2px rgba(0, 150, 255, 0.2) !important;
    }

    /* Back button styles */
    .back-button {
        margin-top: 1rem;
        background: linear-gradient(90deg, #0096FF, #00D4FF);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 50px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    .back-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 150, 255, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"
if "show_login" not in st.session_state:
    st.session_state.show_login = False
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

def go_to(page_name):
    st.session_state.page = page_name

# Sidebar for authentication
with st.sidebar:
    st.markdown("""
        <div class='sidebar-auth'>
            <h1>👤 Account</h1>
    """, unsafe_allow_html=True)
    
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    
    if st.session_state.current_user:
        st.success(f"Welcome, {st.session_state.current_user}!")
        if st.button("Logout", key="logout_btn"):
            logout()
            st.rerun()
    else:
        st.markdown("<div class='sidebar-buttons'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Login", key="show_login_btn"):
                st.session_state.show_login = True
                st.session_state.show_signup = False
        with col2:
            if st.button("Sign Up", key="show_signup_btn"):
                st.session_state.show_signup = True
                st.session_state.show_login = False
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Login form
if st.session_state.show_login:
    st.markdown("""
        <div style='background-color: #2D2D2D; padding: 0.5rem; border-radius: 15px 15px 0 0; text-align: center; margin: 0;'>
            <h2 style='color: #0096FF; font-size: 1.5rem; margin: 0;'>Login</h2>
        </div>
    """, unsafe_allow_html=True)
    with st.form("login_form", clear_on_submit=True):
        st.markdown("<div class='auth-form' style='margin-top: 0; border-radius: 0 0 15px 15px;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top: 0.5rem; margin-bottom: 1rem;'>Welcome Back! 👋</h3>", unsafe_allow_html=True)
        login_username = st.text_input("Username", placeholder="Enter your username")
        login_password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit_login = st.form_submit_button("LOGIN")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if submit_login:
            success, message = login(login_username, login_password)
            if success:
                st.success(message)
                st.session_state.show_login = False
                st.rerun()
            else:
                st.error(message)

# Signup form
if st.session_state.show_signup:
    st.markdown("""
        <div style='background-color: #2D2D2D; padding: 0.5rem; border-radius: 15px 15px 0 0; text-align: center; margin: 0;'>
            <h2 style='color: #0096FF; font-size: 1.5rem; margin: 0;'>Signup</h2>
        </div>
    """, unsafe_allow_html=True)
    with st.form("signup_form", clear_on_submit=True):
        st.markdown("<div class='auth-form' style='margin-top: 0; border-radius: 0 0 15px 15px;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='margin-top: 0.5rem; margin-bottom: 1rem;'>Create Account 🧾</h3>", unsafe_allow_html=True)
        signup_username = st.text_input("Username", placeholder="Choose a username")
        signup_password = st.text_input("Password", type="password", placeholder="Create a strong password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
        submit_signup = st.form_submit_button("CREATE ACCOUNT")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if submit_signup:
            if signup_password != confirm_password:
                st.error("Passwords do not match")
            else:
                success, message = signup(signup_username, signup_password)
                if success:
                    st.success(message)
                    st.session_state.show_signup = False
                    st.rerun()
                else:
                    st.error(message)

# Main content
if st.session_state.page == "home":
    # Clear any previous states
    if 'welcome_shown' not in st.session_state:
        st.session_state.welcome_shown = False
        
    if not st.session_state.welcome_shown:
        st.markdown("""
            <div style='text-align: center; padding: 2rem; background-color: #2D2D2D; border-radius: 10px; margin-bottom: 2rem;'>
                <h2 style='color: #0096FF;'>Welcome to your AI Assistant!</h2>
                <p style='color: #FFFFFF;'>Choose a service below to get started.</p>
            </div>
        """, unsafe_allow_html=True)
        st.session_state.welcome_shown = True

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class='service-card'>
                <h3>
                    <span class='service-card-icon'>👨‍⚖️</span>
                    <span style='background: linear-gradient(90deg, #0096FF, #00D4FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Local Law Teller</span>
                </h3>
                <p>Get simplified legal info tailored to your region. Ask questions about laws, regulations, and legal procedures.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Law Bot", key="law_bot_btn"):
            go_to("law_bot")

    with col2:
        st.markdown("""
            <div class='service-card'>
                <h3>
                    <span class='service-card-icon'>🎓</span>
                    <span style='background: linear-gradient(90deg, #0096FF, #00D4FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Scholarship Checker</span>
                </h3>
                <p>Find scholarships worldwide based on your background. Discover opportunities that match your profile and goals.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Scholarship Bot", key="scholar_bot_btn"):
            go_to("scholarship_bot")

elif st.session_state.page == "law_bot":
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🔙", key="back_home_law"):
            go_to("home")
    
    st.markdown("""
        <div class='chat-header'>
            <h1>🧑‍⚖️ Local Law Chatbot</h1>
            <p>Get simplified legal info tailored to your region. Ask questions about laws, regulations, and legal procedures.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Chat interface
    if 'law_messages' not in st.session_state:
        st.session_state.law_messages = []

    for message in st.session_state.law_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask your legal question..."):
        st.session_state.law_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = f"I received your legal question: {prompt}"
            st.markdown(response)
            st.session_state.law_messages.append({"role": "assistant", "content": response})

elif st.session_state.page == "scholarship_bot":
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🔙", key="back_home_scholar"):
            go_to("home")
    
    st.markdown("""
        <div class='chat-header'>
            <h1>🎓 Scholarship Bot</h1>
            <p>Find scholarships worldwide based on your background. Discover opportunities that match your profile and goals.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Chat interface
    if 'scholar_messages' not in st.session_state:
        st.session_state.scholar_messages = []

    for message in st.session_state.scholar_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about scholarships..."):
        st.session_state.scholar_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = f"Thanks for your interest in scholarships! I received your question: {prompt}"
            st.markdown(response)
            st.session_state.scholar_messages.append({"role": "assistant", "content": response})
