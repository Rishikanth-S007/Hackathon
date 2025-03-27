import streamlit as st
import streamlit.components.v1 as components

def create_speech_recognition_component():
    """Creates a speech recognition component using the Web Speech API"""
    components.html(
        """
        <div style="display: flex; align-items: center; gap: 10px;">
            <button id="startButton" style="
                background-color: #0096FF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
            ">
                🎙️ Start Recording
            </button>
            <p id="status" style="color: white; margin: 0;"></p>
        </div>
        <script>
            const startButton = document.getElementById('startButton');
            const status = document.getElementById('status');
            let recognition = null;
            
            if ('webkitSpeechRecognition' in window) {
                recognition = new webkitSpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                
                recognition.onstart = () => {
                    startButton.style.backgroundColor = '#ff4b4b';
                    startButton.textContent = '🔴 Stop Recording';
                    status.textContent = 'Listening...';
                };
                
                recognition.onresult = (event) => {
                    const transcript = event.results[0][0].transcript;
                    window.parent.postMessage({type: 'speech-recognition', text: transcript}, '*');
                    status.textContent = 'Processing...';
                };
                
                recognition.onend = () => {
                    startButton.style.backgroundColor = '#0096FF';
                    startButton.textContent = '🎙️ Start Recording';
                    status.textContent = '';
                };
                
                startButton.onclick = () => {
                    if (recognition.state === 'inactive') {
                        recognition.start();
                    } else {
                        recognition.stop();
                    }
                };
            } else {
                startButton.disabled = true;
                status.textContent = 'Speech recognition not supported in this browser.';
            }
        </script>
        """,
        height=70,
    )

def transcribe_audio():
    """Creates a voice input interface using the Web Speech API"""
    create_speech_recognition_component()
    
    # Create a placeholder for the transcribed text
    result_placeholder = st.empty()
    
    # JavaScript message handling
    if 'transcribed_text' not in st.session_state:
        st.session_state.transcribed_text = None
    
    return st.session_state.transcribed_text
