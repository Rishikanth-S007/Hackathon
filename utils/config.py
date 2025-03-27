import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8000')  # Default to localhost if not set

# API Endpoints
AUTH_ENDPOINT = f"{API_BASE_URL}/api/auth"
LAW_BOT_ENDPOINT = f"{API_BASE_URL}/api/law"
SCHOLARSHIP_BOT_ENDPOINT = f"{API_BASE_URL}/api/scholarship" 