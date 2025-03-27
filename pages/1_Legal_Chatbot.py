import streamlit as st
from utils.voice_input import transcribe_audio

st.title("🧑‍⚖️ Local Law Teller")

st.markdown("""
    <div style='padding: 1rem; background-color: #2D2D2D; border-radius: 10px; margin-bottom: 1rem;'>
        <p style='color: #FFFFFF;'>Ask any legal question and get simplified answers tailored to your region.</p>
    </div>
""", unsafe_allow_html=True)

# Initialize session state for messages
if 'legal_messages' not in st.session_state:
    st.session_state.legal_messages = []

# Voice input section with custom styling
st.markdown("""
    <div style='margin-bottom: 1rem;'>
        <h3 style='color: #0096FF;'>Voice Input</h3>
        <p style='color: #FFFFFF;'>Click the button below to start recording your question</p>
    </div>
""", unsafe_allow_html=True)

# Handle voice input
transcript = transcribe_audio()
if transcript:
    st.session_state.legal_messages.append({
        "role": "user",
        "content": transcript
    })
    # Add AI response
    response = f"I received your legal question: {transcript}"
    st.session_state.legal_messages.append({
        "role": "assistant",
        "content": response
    })
    st.rerun()

# Display chat history
for message in st.session_state.legal_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Text input for typing questions
if prompt := st.chat_input("Type your legal question..."):
    st.session_state.legal_messages.append({
        "role": "user",
        "content": prompt
    })
    # Add AI response
    response = f"I received your legal question: {prompt}"
    st.session_state.legal_messages.append({
        "role": "assistant",
        "content": response
    })
    st.rerun()

# Back button
if st.button("🔙 Back to Home"):
    st.switch_page("app.py")
