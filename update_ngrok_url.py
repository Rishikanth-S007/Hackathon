import os
import re
import time
from pathlib import Path

def extract_ngrok_url():
    """Extract the ngrok URL from the ngrok web interface"""
    try:
        import requests
        response = requests.get('http://localhost:4040/api/tunnels')
        if response.status_code == 200:
            tunnels = response.json()['tunnels']
            for tunnel in tunnels:
                if tunnel['proto'] == 'https':
                    return tunnel['public_url']
    except:
        pass
    return None

def update_env_file():
    """Update the .env file with the new ngrok URL"""
    env_path = Path(__file__).parent / '.env'
    ngrok_url = extract_ngrok_url()
    
    if ngrok_url:
        if env_path.exists():
            with open(env_path, 'r') as f:
                content = f.read()
            
            # Update or add API_BASE_URL
            if 'API_BASE_URL=' in content:
                content = re.sub(r'API_BASE_URL=.*', f'API_BASE_URL={ngrok_url}', content)
            else:
                content += f'\nAPI_BASE_URL={ngrok_url}'
            
            with open(env_path, 'w') as f:
                f.write(content)
            print(f"Updated .env file with new ngrok URL: {ngrok_url}")
        else:
            with open(env_path, 'w') as f:
                f.write(f'API_BASE_URL={ngrok_url}')
            print(f"Created .env file with ngrok URL: {ngrok_url}")

if __name__ == "__main__":
    print("Waiting for ngrok to start...")
    while True:
        update_env_file()
        time.sleep(5)  # Check every 5 seconds 