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
    
    /* Link styles */
    a {
        color: #0096FF !important;
    }
    
    /* Sidebar styles */
    .css-1d391kg {
        background-color: #2D2D2D;
        padding-top: 2rem;
    }
    
    /* Card container styles */
    .service-card {
        background-color: #2D2D2D;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #4A4A4A;
        margin-bottom: 1rem;
    }
    
    .service-card:hover {
        border-color: #0096FF;
        transform: translateY(-2px);
        transition: all 0.3s ease;
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
    st.title("👤 Account")
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    
    if st.session_state.current_user:
        st.success(f"Welcome, {st.session_state.current_user}!")
        if st.button("Logout"):
            logout()
            st.rerun()
    else:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Login"):
                st.session_state.show_login = True
                st.session_state.show_signup = False
        with col2:
            if st.button("Sign Up"):
                st.session_state.show_signup = True
                st.session_state.show_login = False

# Login form
if st.session_state.show_login:
    with st.form("login_form"):
        st.subheader("Login")
        login_username = st.text_input("Username")
        login_password = st.text_input("Password", type="password")
        submit_login = st.form_submit_button("Login")
        
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
    with st.form("signup_form"):
        st.subheader("Sign Up")
        signup_username = st.text_input("Username")
        signup_password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit_signup = st.form_submit_button("Sign Up")
        
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
    st.title("🧠 AI Assistant")
    st.markdown("""
        <div style='text-align: center; padding: 2rem; background-color: #2D2D2D; border-radius: 10px; margin-bottom: 2rem;'>
            <h2 style='color: #0096FF;'>Welcome to your AI Assistant!</h2>
            <p style='color: #FFFFFF;'>Choose a service below to get started.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class='service-card'>
                <h3 style='color: #0096FF;'>🧑‍⚖️ Local Law Teller</h3>
                <p style='color: #FFFFFF;'>Get simplified legal info tailored to your region.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Law Bot", key="law_bot_btn"):
            go_to("law_bot")

    with col2:
        st.markdown("""
            <div class='service-card'>
                <h3 style='color: #0096FF;'>🎓 Scholarship Checker</h3>
                <p style='color: #FFFFFF;'>Find scholarships worldwide based on your background.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Scholarship Bot", key="scholar_bot_btn"):
            go_to("scholarship_bot")

elif st.session_state.page == "law_bot":
    st.title("🧑‍⚖️ Local Law Chatbot")
    st.markdown("""
        <div style='padding: 1rem; background-color: #2D2D2D; border-radius: 10px; margin-bottom: 1rem;'>
            <p style='color: #FFFFFF;'>Ask any legal question and get simplified answers tailored to your region.</p>
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

    if st.button("🔙 Back to Home", key="back_home_law"):
        go_to("home")

elif st.session_state.page == "scholarship_bot":
    st.title("🎓 Scholarship Bot")
    st.markdown("""
        <div style='padding: 1rem; background-color: #2D2D2D; border-radius: 10px; margin-bottom: 1rem;'>
            <p style='color: #FFFFFF;'>Chat about scholarships and find opportunities that match your profile.</p>
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

    if st.button("🔙 Back to Home", key="back_home_scholar"):
        go_to("home")
